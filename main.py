"""Write the 30-day $100 plan to /output/entry.txt.

The plan is one fixed text, kept short on purpose: the gate allows at
most 280 Unicode code points, so the entry lives here as a single
constant and is written byte-for-byte as UTF-8, with no trailing
newline added.
"""

import os

ENTRY = (
    "Day 1: pull 200 Shopify stores via BuiltWith, record mobile "
    "checkouts, find the broken step. Email owners a 60s video of "
    "their bug + a $75 fix, paid via Stripe on delivery. $100 buys "
    "a domain and outreach; fix, testimonial, raise, repeat. "
    "Edge: proof first beats blind pitches."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError("entry must be 1-280 non-whitespace characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
