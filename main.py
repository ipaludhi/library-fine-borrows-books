# One Line, Big Laugh — entry program (Python 3.13, stdlib only).
# Writes one original one-line joke to /output/entry.txt.
# The joke: a library fine so old it has grown up and become a borrower
# itself — it turns up asking for a card and proof of address.
import os
from pathlib import Path

JOKE = "My library fine is now old enough to borrow books itself - it asked for a card and proof of address."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
# Gate self-check: 1-200 chars, not whitespace-only, single line.
if not 1 <= len(JOKE) <= 200 or not JOKE.strip() or "\n" in JOKE:
    raise SystemExit(f"joke fails gate, {len(JOKE)} chars")
(out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
