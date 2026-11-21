"""Refresh the snapshot from the live record: download the two files, update the counts in the README, add a line to CHANGES.
Prints the release tag (date.n) when something changed, nothing otherwise."""
import csv, datetime, io, re, subprocess, sys, urllib.request

SITE = "https://tallycatalog.com"


def get(path):
    req = urllib.request.Request(SITE + path, headers={"User-Agent": "tally-data release (github.com/verkyyi/tally-data)"})
    return urllib.request.urlopen(req, timeout=300).read().decode("utf-8")


numbers, history = get("/data/numbers.csv"), get("/data/history.csv")
n = list(csv.DictReader(io.StringIO(numbers)))
h = sum(1 for _ in csv.DictReader(io.StringIO(history)))
subjects = len({r.get("subject") or r["title"].split(" · ")[0] for r in n})
if len(n) < 500 or h < 30000:  # a short answer from the site is an error, not a release
    sys.exit(f"refusing to release: {len(n)} numbers, {h} values")

open("numbers.csv", "w").write(numbers)
open("history.csv", "w").write(history)
if not subprocess.run(["git", "status", "--porcelain", "numbers.csv", "history.csv"], capture_output=True, text=True).stdout.strip():
    sys.exit(0)
today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
readme = open("README.md").read()
readme, k = re.subn(r"[\d,]+ numbers about [\d,]+ companies and\nopen-source projects, with [\d,]+ dated values",
                    f"{len(n):,} numbers about {subjects:,} companies and\nopen-source projects, with {h:,} dated values", readme)
readme = re.sub(r"Snapshot date: \d{4}-\d{2}-\d{2}", f"Snapshot date: {today}", readme)
open("README.md", "w").write(readme)
tags = subprocess.run(["git", "tag", "--list"], capture_output=True, text=True).stdout.split()
last = max([int(t.rsplit(".", 1)[1]) for t in tags if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.\d+", t)] or [0])
tag = f"{today}.{last + 1}"
changes = open("CHANGES.md").read()
entry = f"# Changes\n\n## {today} (release {last + 1})\n\n- Snapshot of the live record: {len(n):,} numbers about {subjects:,} companies and open-source projects, {h:,} dated values.\n"
open("CHANGES.md", "w").write(entry + changes[len("# Changes\n"):] if changes.startswith("# Changes\n") else entry + "\n" + changes)
print(tag)
