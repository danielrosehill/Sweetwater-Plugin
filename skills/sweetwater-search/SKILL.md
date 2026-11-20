---
name: sweetwater-search
description: Find products on Sweetwater by need or model list: Exa queries, category and brand URLs, reading category rows and deals.
---

# Sweetwater search

## Steps

1. **One `web_search_exa` per model or need**, querying "<model> sweetwater.com". The highlights usually include the product page text.
2. **Category sweeps.** Category pages list every item, with price, rating, stock and deal rows.
   - Category URL: `https://www.sweetwater.com/c<NNNN>--<Name>`, e.g. `/c1175--Broadcast_Headset_Microphones`.
   - Brand within a category: `/c1175--<Brand>_<Category>`, e.g. `/c1175--Beyerdynamic_Broadcast_Headset_Microphones`.
   - Brand pages: `/brand/<brand>`, `/brand/<brand>/series/<series>`, `/store/manufacturer/<Brand>`.
   - Fetch these with `web_fetch_exa`.
   - Category rows show the price, an optional financing line (ignore it), "Certified Open Box available for $X", "Rated 4.5/5 Stars (N)" and the stock status.
   - The sidebar counts deals: "Certified Open Box (N), Used (N), Demos (N)".
3. **Search URL:** `https://www.sweetwater.com/store/search?s=<terms>`. Exa often times out on it live. Prefer step 1.
4. Filter and sort query parameters were unverified on 2026-11-20. Don't guess them.
5. **Absence is weak evidence.** An item missing from a cached category may be new since the crawl. Say "not found in cached pages", not "not sold".
6. Pass the shortlist to `sweetwater-listing-check`.
