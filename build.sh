#!/bin/sh
# Build "Is the Riemann Hypothesis Solved?" to PDF.
# Usage: ./build.sh
set +e
cd "$(dirname "$0")"
SRC=source
OUT=output
mkdir -p "$OUT"

# 0. make the book fonts available to fontconfig (Outfit, JetBrains Mono)
mkdir -p "$HOME/.fonts"
cp fonts/Outfit-*.ttf fonts/JetBrainsMono-*.ttf "$HOME/.fonts/" 2>/dev/null || true
fc-cache -f >/dev/null 2>&1 || true

# 1. word count from the book's own source text
python3 - <<'PY'
import re, pathlib
src = pathlib.Path("source")
files = sorted(src.glob("chapters/*.tex")) + [src/"frontmatter.tex", src/"backmatter.tex"]
words = 0
for f in files:
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?", " ", t)
    t = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", t)
    t = re.sub(r"[{}$^_&~\\]", " ", t)
    t = re.sub(r"\s+", " ", t)
    words += len([w for w in t.split() if re.search(r"[A-Za-z0-9]", w)])
pathlib.Path("source/generated.tex").write_text(
    "\\newcommand{\\bookPages}{PLACEHOLDER_PAGES}\n"
    "\\newcommand{\\bookWords}{PLACEHOLDER_WORDS}\n", encoding="utf-8")
print("body word count:", words)
pathlib.Path("source/.wordcount").write_text(str(words), encoding="utf-8")
PY

# 2. typeset
cd "$SRC"
xelatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null || true
xelatex -interaction=nonstopmode main.tex >/dev/null
if [ -f main.aux ]; then makeindex -q main.idx 2>/dev/null || true; fi
xelatex -interaction=nonstopmode main.tex >/dev/null
xelatex -interaction=nonstopmode main.tex >/dev/null

# 3. page count, then refresh the colophon
TOTAL=$(pdfinfo main.pdf | awk '/^Pages:/{print $2}')
PAGES=$((TOTAL - 2))   # exclude the front and back cover leaves
WORDS=$(cat .wordcount)
python3 - "$PAGES" "$WORDS" <<'PY'
import sys, pathlib
pages, words = sys.argv[1], int(sys.argv[2])
formatted = f"{words:,}"
pathlib.Path("generated.tex").write_text(
    "\\newcommand{\\bookPages}{" + pages + "}\n"
    "\\newcommand{\\bookWords}{" + formatted + "}\n", encoding="utf-8")
PY
xelatex -interaction=nonstopmode main.tex >/dev/null
xelatex -interaction=nonstopmode main.tex >/dev/null
cd ..
cp "$SRC/main.pdf" "$OUT/Is-the-Riemann-Hypothesis-Solved.pdf"
echo "PAGES=$PAGES (of $TOTAL including covers)  WORDS=$WORDS"
pdfinfo "$OUT/Is-the-Riemann-Hypothesis-Solved.pdf" | head -12
