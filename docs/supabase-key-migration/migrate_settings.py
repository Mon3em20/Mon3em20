#!/usr/bin/env python3
"""Move the Supabase URL and key in config/settings.py to environment variables.

Run this LOCALLY inside a clone of Library-Management-System:

    python3 migrate_settings.py path/to/config/settings.py

What it does:
  * replaces the right-hand side of the top-level `url = ...` and `key = ...`
    assignments with os.environ["SUPABASE_URL"] / os.environ["SUPABASE_KEY"];
  * adds `import os` if it is missing;
  * keeps a backup next to the file (settings.py.bak) so you can compare locally.

It never prints the old values. It only reports line numbers and variable names.
The backup file CONTAINS the old key: delete it (or keep it untracked) and never commit it.
Do not paste the output of `git diff` for this file into chats, issues or PRs, because
the diff shows the removed line.
"""
import re
import shutil
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "config/settings.py"
src = open(path, encoding="utf-8").read()
lines = src.splitlines()

targets = {"url": "SUPABASE_URL", "key": "SUPABASE_KEY"}
changed = []
for i, line in enumerate(lines):
    m = re.match(r"^(url|key)\s*=\s*\S", line)
    if m:
        name = m.group(1)
        lines[i] = f'{name} = os.environ["{targets[name]}"]'
        changed.append((i + 1, name))

if {n for _, n in changed} != set(targets):
    sys.exit("Expected top-level `url = ...` and `key = ...` assignments; nothing was changed.")

if not any(re.match(r"^\s*import os\b", l) for l in lines):
    lines.insert(0, "import os")

shutil.copyfile(path, path + ".bak")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
for ln, name in changed:
    print(f"line {ln}: `{name}` now reads {targets[name]} from the environment")
print("Backup written to", path + ".bak", "(contains the old values: do not commit it)")
