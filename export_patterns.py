"""Write patterns.json from the list in guard.py, for the browser-only demo on GitHub Pages."""
import json
from pathlib import Path

import guard

out = Path(__file__).parent / "patterns.json"
out.write_text(json.dumps(guard.injections, indent=2) + "\n")
print(f"Wrote {len(guard.injections)} patterns to {out.name}")
