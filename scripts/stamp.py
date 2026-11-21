#!/usr/bin/env python3
"""Mark a content update: set SITE_UPDATED in data/data.js (default: today) and bump the
?v= cache-busting stamps in index.html so browsers load the new files.

    python3 scripts/stamp.py              # today
    python3 scripts/stamp.py 2027-03-15   # a specific date
"""
import os, re, sys, time
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
day = sys.argv[1] if len(sys.argv) > 1 else time.strftime("%Y-%m-%d")
assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", day), "date must be YYYY-MM-DD"
p = os.path.join(root, "data", "data.js"); s = open(p).read()
s, n = re.subn(r'const SITE_UPDATED = "[^"]*";', f'const SITE_UPDATED = "{day}";', s); assert n == 1
open(p, "w").write(s)
p = os.path.join(root, "index.html"); h = open(p).read()
v = time.strftime("%Y%m%d%H%M"); h, m = re.subn(r"\?v=\d+", "?v=" + v, h)
open(p, "w").write(h)
print(f"SITE_UPDATED = {day}; {m} asset stamps set to v={v}")
