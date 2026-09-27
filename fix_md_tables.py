import re, sys, io, shutil

def fix(path):
    raw = io.open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    out, i, changed = [], 0, False
    row_re = re.compile(r"^\s*\|.*\|\s*$")
    sep_re = re.compile(r"^\s*\|[\s:\-|]+\|\s*$")
    while i < len(lines):
        line = lines[i]
        if row_re.match(line) and not sep_re.match(line):
            block = []
            while i < len(lines) and row_re.match(lines[i]) and not sep_re.match(lines[i]):
                block.append(lines[i]); i += 1
            def clean(r):
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                return "| " + " | ".join(cells) + " |"
            block = [clean(b) for b in block]
            ncol = block[0].count("|") - 1
            sep = "|" + "|".join([" --- " for _ in range(ncol)]) + "|"
            out.append(block[0]); out.append(sep); out.extend(block[1:])
            changed = True
        else:
            out.append(line); i += 1
    if changed:
        shutil.copy(path, path + ".bak2")
        io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    return changed

for p in sys.argv[1:]:
    print(("FIXED " if fix(p) else "skip  ") + p)
