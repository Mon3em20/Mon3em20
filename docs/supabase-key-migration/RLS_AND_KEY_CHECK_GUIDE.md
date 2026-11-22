# Supabase: RLS, Permissions and Key Check Guide

For the project used by `Library-Management-System`. Do these checks **before** deciding whether to migrate or deactivate the API key. Nothing here rotates a key or changes data. Never paste a key into chat, issues, PRs or terminal history; use environment variables.

## 1. Which key was committed

Verified from the token's own (public) claims, without printing it: the committed key is a **legacy JWT-style `anon` key** (`role` claim = `anon`, issued 2025-07-30, expires 2035-07-30).

| Key kind | Meant for | Bypasses RLS? | Safe in a public repo? |
|---|---|---|---|
| Legacy `anon` JWT (this one) / newer "publishable" key | Browser and mobile clients | No, it is subject to RLS and table grants | Acceptable by design **only if** RLS and grants are correct; still better kept out of the repo |
| Legacy `service_role` JWT / newer "secret" key | Servers only | **Yes**, full access | Never |
| JWT signing secret | Project administrator | n/a (it can mint any key) | Never |

No `service_role` or secret key was found in the repository. Check the Supabase dashboard's current API-key documentation for the exact names in your project, as they have changed over time.

## 2. Check Row Level Security (SQL editor, read-only queries)

Which tables in `public` have RLS enabled (every row should be `true`):

```sql
select schemaname, tablename, rowsecurity
from pg_tables
where schemaname = 'public'
order by tablename;
```

All policies, to read for over-broad rules such as `using (true)` applied to `anon` or `public`:

```sql
select tablename, policyname, roles, cmd, qual, with_check
from pg_policies
where schemaname = 'public'
order by tablename, policyname;
```

Table privileges granted to the API roles (look for `anon` holding INSERT, UPDATE, DELETE or TRUNCATE):

```sql
select table_name, grantee, privilege_type
from information_schema.role_table_grants
where table_schema = 'public' and grantee in ('anon', 'authenticated')
order by table_name, grantee, privilege_type;
```

Also review: views (views run with their owner's rights unless created `security_invoker`), `security definer` functions exposed through the API, and storage bucket policies (Storage, then Policies).

Dashboard shortcut: open **Database, then Advisors** (Security Advisor) and resolve every "RLS disabled" and "policy exists but RLS disabled" finding.

## 3. Test what an anonymous caller can do (safely)

Run from your own terminal with the values in environment variables, never typed inline into shared history:

```bash
export SUPABASE_URL=...        # from your project settings
export SUPABASE_KEY=...        # the anon key
curl -s "$SUPABASE_URL/rest/v1/<table>?select=*&limit=1" \
  -H "apikey: $SUPABASE_KEY" -H "Authorization: Bearer $SUPABASE_KEY"
```

Expected for a protected table: an empty list or a permission error. If it returns real rows or accepts a write, the table is exposed. Repeat for each table.

## 4. Review activity
In the dashboard open **Logs**, then API and Postgres logs, and look for requests you do not recognize since 2025-07-30. If the project holds only test data, deleting the project is the simplest remedy.

## 5. Decide, then act (all of these are yours to approve)

| Finding | Suggested action |
|---|---|
| RLS enabled everywhere, restrictive policies, no unexpected activity | Low risk. Migrate the code to environment variables and optionally rotate or deactivate the key later |
| RLS disabled or policies too open | Fix the policies first (this is the real exposure), then rotate or deactivate the key |
| Test data only | Delete the project, or rotate and migrate |

Rotation notes: rotating the legacy JWT signing secret invalidates the `anon` **and** `service_role` keys and existing sessions at once, so every app using them breaks until updated. Newer Supabase API keys can be created and revoked individually, which is gentler; read the current Supabase documentation for your project before choosing. This guide and the migration script do **not** rotate or revoke anything.

## 6. Code migration (prepared, not applied)

`migrate_settings.py` (same folder) rewrites `config/settings.py` locally so that `url` and `key` read `SUPABASE_URL` and `SUPABASE_KEY` from the environment. It never prints the old values and writes a local `.bak` backup that you must delete or leave untracked. After PR "Untrack empty .env; add .gitignore and .env.example" is merged:

```bash
cp .env.example .env              # then fill in values; .env is git-ignored
python3 migrate_settings.py config/settings.py
rm config/settings.py.bak         # after checking the file locally
```

The app must then load the variables (for example `export $(grep -v '^#' .env | xargs)`, or `python-dotenv` if you choose to add it as a dependency). The old value stays in Git history until history is cleaned, which is a separate step that needs your approval (see `ACTION_PLANS.md`). Do not post `git diff` output for this file anywhere, because the diff shows the removed line.
