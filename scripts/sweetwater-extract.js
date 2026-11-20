// Sweetwater product-page extractor for a real browser tab (CDP evaluate / claude-in-chrome javascript_tool).
// STATUS 2026-11-20: syntax-checked and its regexes tested on cached page text only. Every live
// route tried from a non-US connection hit the HUMAN Security (PerimeterX) captcha, so this has
// NOT run on a live Sweetwater DOM. It returns {blocked:true} on the captcha page.
() => {
  const out = { url: location.href, title: document.title,
    blocked: /denied|just a moment|captcha/i.test(document.title) };
  if (out.blocked) return out;
  const txt = s => (s || '').replace(/\s+/g, ' ').trim();
  for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
    try {
      const j = JSON.parse(s.textContent);
      for (const n of [].concat(j['@graph'] || j)) {
        if (n && /Product/.test([].concat(n['@type']).join())) {
          const o = [].concat(n.offers || [])[0] || {};
          out.ld = { name: n.name, sku: n.sku, mpn: n.mpn, price: o.price || o.lowPrice,
            currency: o.priceCurrency, availability: o.availability, itemCondition: o.itemCondition };
        }
      }
    } catch (e) {}
  }
  const m = location.pathname.match(/\/store\/detail\/([^\/-][^\/]*?)(?:--|\/|$)/);
  out.itemId = m && m[1];
  const h1 = document.querySelector('h1');
  out.h1 = txt(h1 && h1.textContent);
  const scope = (h1 && (h1.closest('main') || h1.parentElement.parentElement)) || document.body;
  const t = txt(scope.innerText).replace(/\$\s?[\d.,]+\s?\/\s?mo(nth)?\S*/gi, '');   // drop financing
  out.pricesInOrder = [...t.matchAll(/\$\s?[\d,]+(?:\s?\.\s?\d{2})?/g)].map(x => x[0].replace(/\s/g, '')).slice(0, 6);
  const stock = t.match(/(In Stock!?(?: Only \d+ left in stock!?[^.]*)?|We Can Get It Fast!|Backordered[^.]*|Ships in [^.]*|Estimated [A-Z][a-z]+ \d+, \d{4}|no longer available|Out of Stock|Call for availability)/i);
  out.stock = stock && stock[0];
  out.openBox = (t.match(/Certified Open Box available for \$[\d,.]+/i) || [])[0] || null;
  out.usedGearExchange = (t.match(/Used[^$]{0,40}\$[\d,.]+/) || [])[0] || null;
  out.addToCartToSeePrice = /add to cart to see (the )?price|see price in cart/i.test(t) || null;
  return out;
}
