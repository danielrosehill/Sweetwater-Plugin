#!/usr/bin/env python3
"""Parse Exa markdown of Sweetwater product pages into JSON.

Sweetwater renders prices as "$ 239 .00 239 dollars and 0 cents", shows financing figures
("$5.08/month") that are not the price, and keeps discontinued pages up with a stale price.
Exa content is a cache of unknown age; every record is tagged source=exa-cache.

Usage: python3 parse_exa_sweetwater.py page.md   (or stdin). One JSON object per "URL:" block.
"""
import json
import re
import sys

FINANCING = re.compile(r"\$\s?[\d.,]+\s?/\s?mo(?:nth)?\S*[^\n]*", re.I)
SW_PRICE = re.compile(r"\$\s?([\d,]+)\s?(?:\.\s?(\d{2}))?")
STOCK = re.compile(
    r"In Stock!?(?:\s*Only \d+ left in stock!?)?|We Can Get It Fast!|Backordered[^\n]{0,60}|"
    r"Ships in [^\n]{0,40}|Estimated [A-Z][a-z]+ \d+, \d{4}|no longer available|Out of Stock|Call for availability",
    re.I,
)


def parse_block(text: str) -> dict:
    url = (re.search(r"^URL:\s*(\S+)", text, re.M) or [None, None])[1]
    title = (re.search(r"^#\s+(.+?)(?:\s*\|\s*Sweetwater)?$", text, re.M) or [None, None])[1]
    item = re.search(r"/store/detail/([^/\-?#][^/?#]*?)(?:--|/|$|\?)", url or "")
    item_id = re.search(r"Item ID:\s*(\S+)", text)
    clean = FINANCING.sub("", text)
    clean = re.sub(r"Special Financing[^\n]*", "", clean)
    discontinued = bool(re.search(r"no longer available", clean, re.I))
    prices = []
    for m in SW_PRICE.finditer(clean):
        dollars, cents = m.group(1).replace(",", ""), m.group(2) or "00"
        prices.append(f"{dollars}.{cents}")
    stock = STOCK.search(clean)
    open_box = re.search(r"Certified Open Box available for \$\s?([\d,]+(?:\.\d{2})?)", clean, re.I)
    estimated = re.search(r"Estimated ([A-Z][a-z]+ \d+, \d{4})", clean)
    return {
        "url": url,
        "title": title,
        "item_id": (item_id.group(1) if item_id else None) or (item.group(1) if item else None),
        "price_first_seen": None if discontinued else (prices[0] if prices else None),
        "prices_in_order": prices[:8],
        "stock": "no longer available" if discontinued else (re.sub(r"\s+", " ", stock.group(0)).strip() if stock else None),
        "special_order_estimate": estimated.group(1) if estimated else None,
        "discontinued": discontinued,
        "no_cable_note": bool(re.search(r"does not include a (connection )?cable|\bLess Cable\b|-LC\b", clean, re.I)),
        "open_box": open_box.group(1).replace(",", "") if open_box else None,
        "source": "exa-cache",
        "warning": "Cached copy of unknown age; live sweetwater.com is behind a bot wall. Verify before buying.",
    }


def main() -> None:
    data = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    blocks = re.split(r"(?=^# .+\nURL:)", data, flags=re.M)
    print(json.dumps([parse_block(b) for b in blocks if re.search(r"^URL:", b, re.M)], indent=2))


if __name__ == "__main__":
    main()
