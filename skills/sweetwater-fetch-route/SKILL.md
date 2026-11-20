---
name: sweetwater-fetch-route
description: How to reach Sweetwater (sweetwater.com) despite its HUMAN/PerimeterX bot wall: Exa cache first, cache-age warnings, live checks.
---

# Reaching Sweetwater

Live sweetwater.com sits behind HUMAN Security (formerly PerimeterX). Blocked requests get HTTP 403, the title
"Access to this page has been denied" and a `px-captcha` page. Field test, 2026-11-20, from a non-US connection:

| Route | Result |
|---|---|
| Built-in WebFetch | 403 |
| curl, from a laptop and from a separate server | 403, captcha page |
| Playwright/agent browsers (two profiles) | 403 |
| The user's real Chrome (extension) | Blocked: no page content, no JSON-LD |
| Exa `web_search_exa` | Works, returns **cached** pages |
| Exa `web_fetch_exa` | Works on most product URLs. `CRAWL_LIVECRAWL_TIMEOUT` on search URLs and on some guessed ones |

## Rules

1. **Exa is the default route, and it is a cache.** Ages vary per page:
   - The same product showed $239 in one copy and $219 in another.
   - A category page said "In Stock" while the product page said "no longer available".
   - Direct product pages (`/store/detail/<ITEMID>`) looked fresher than category or search pages.
   - Tag every figure `source: exa-cache` and give the date you read it.
2. **Live verification.** Untested ideas:
   - A real browser from a US residential connection.
   - Asking the user to open the page.
   - Calling Sweetwater on +1 800 222-4700. Their Sales Engineers quote price and stock.

   Don't claim a live check you didn't make.
3. **Don't hammer the wall.** Repeated blocked requests add nothing. After one blocked live attempt per route, go back to Exa.
4. **Item IDs.** Product URLs work without the slug: `https://www.sweetwater.com/store/detail/BPHS1`.
   - The ID is usually the manufacturer part number with punctuation stripped (`BRH440M-LC` → `BRH440MLC`).
   - Some IDs aren't guessable (`MVX2U Gen 2` → `MVX2UG2`). If a guess times out, find the URL with `web_search_exa`.
5. If a page does load live, `scripts/sweetwater-extract.js` reads it. It has not been tested on a live DOM. Report that if you use it.
