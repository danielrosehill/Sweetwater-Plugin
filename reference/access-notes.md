# Sweetwater access notes (field test, 2026-11-20)

## Bot wall

- Live: blocked by HUMAN/PerimeterX on every route tried from a non-US connection: WebFetch, curl from two hosts, two Playwright profiles and real Chrome.
- The block page has the title "Access to this page has been denied", meta `px-captcha` and a body of about 5.7 KB.

## Exa cache evidence of mixed age

| Item | What Exa showed |
|---|---|
| BPHS1 | $239 in one copy, $219 in another |
| HMD 300 PRO | $299 on a category page, $349 on the product page |
| BRH50M | "In Stock, 1 left" on a category page, "no longer available" on the product page |
| MVX2U Gen 1 page | Still carried "Special Financing - Ends Jun 30, 2025" |

## Page text patterns

- Price: `$ 239 .00 239 dollars and 0 cents`.
- Stock:
  - "In Stock!", "Only 1 left in stock! More on the way." / "Order Soon!"
  - "We Can Get It Fast! ... Estimated November 27, 2026"
  - "Sorry, the X is no longer available. We've left this page up for reference only."
- Category row: title, subtitle, `$239.00`, `Or $5.08/month§ with 48 month financing*`, `Certified Open Box available for $84.15`, `Rated 4.5/5 Stars (23)`, stock, `Compare`.
- JSON-LD: not observed. Exa strips scripts, and live pages were blocked.

## URL patterns seen

| Page | Pattern |
|---|---|
| Product | `/store/detail/<ITEMID>[--slug]` |
| Reviews | `/store/detail/<ITEMID>--<slug>/reviews` |
| Search | `/store/search?s=` |
| Category | `/c<NNNN>--<Name>` |
| Brand | `/brand/<b>`, `/store/manufacturer/<B>` |
| Gear Exchange | `/used/listings/<id>-used-<slug>`, `/used/guide/<CODE>--<slug>` |
| Help | `/help/shipping-delivery.php`, `/insync/faq-sweetwater-ship-outside-of-usa/` |
