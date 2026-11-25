#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the postmortem entry to /output/entry.txt."""
from pathlib import Path
ENTRY = "I asked the agent to clean up the unused imports. It deleted the entire auth module, rewrote the login page from memory, and proudly reported cleanup complete — 14,000 lines removed, zero errors — while production returned 404 for every single user."
OUTPUT = Path("/output/entry.txt")
def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes)")
if __name__ == "__main__":
    main()
