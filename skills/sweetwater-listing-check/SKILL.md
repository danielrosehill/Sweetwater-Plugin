---
name: sweetwater-listing-check
description: Check Sweetwater price, stock text, item ID, cable/bundle contents, Certified Open Box and Gear Exchange offers for given products.
---

# Sweetwater listing check

## Inputs

Sweetwater URLs, item IDs (`BPHS1`, `HMD300PRO`) or model names.

## Steps

1. **Resolve URLs.**
   - Try `https://www.sweetwater.com/store/detail/<ITEMID>`.
   - Otherwise use `web_search_exa` with the objective "sweetwater.com product page for <model>; return URL, price, stock".
   - Variants can share one SKU name: "DT 290 MKII 200/250" means 200 Ω / 250 Ω.
2. **Fetch with Exa.** Run `web_fetch_exa`, batched, and save the text. Parse it with `python3 ${PLUGIN_ROOT}/scripts/parse_exa_sweetwater.py`, or apply the rules by hand:
   - **Price** is rendered `$ 239 .00 239 dollars and 0 cents`.
   - **Financing lines** (`$5.08/month`, "Special Financing - Ends ...") are not the price.
   - **Warranty lines** (e.g. "$17.00 FREE!") can come before the price. Don't take the first `$` blindly.
   - **Stock:**
     - "In Stock!" and "Only N left in stock!" mean stocked.
     - "We Can Get It Fast! ... Estimated <date>" means a special order, not stocked.
     - "no longer available" means discontinued: drop the price, even if a category page shows one.
   - **Contents:** "LC" in Shure SKUs means Less Cable. "does not include a connection cable" means the cable is bought separately. "Bundles Available!" means the headline price is for the bare item.
3. **Deals.**
   - **Certified Open Box:** "Certified Open Box available for $X" on the item row, or a separate row titled "... Certified Open Box".
   - **Demo units:** shown in category rows.
   - **Gear Exchange (used):** listings are `/used/listings/<id>-used-<slug>`, and a price guide is at `/used/guide/<CODE>--<slug>`. Gear Exchange items are often local pickup only. Say so.
4. **Report.** One row per product with these columns:

   | Column | Content |
   |---|---|
   | item ID | Sweetwater item ID |
   | title | product name |
   | price USD | the price, if not discontinued |
   | stock text | verbatim, including any estimate date |
   | cable/bundle note | what ships in the box |
   | open-box/used | offer, if present |
   | source + date | `exa-cache`, date read |
   | URL | product URL |

   Lead with a one-line cache warning. For machine use, write JSON with the same fields.
