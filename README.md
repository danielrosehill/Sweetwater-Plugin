# sweetwater

Marketplace plugin for **Sweetwater** (sweetwater.com), the large US music and pro-audio dealer.

Live Sweetwater pages are behind HUMAN Security (PerimeterX). In testing on 2026-11-20, every direct route was blocked: fetch tools, curl, automated browsers and a real browser from a non-US connection. What does work is Exa's cache of Sweetwater pages. This plugin reads that cache correctly and never lets a cached price pass as a live one. That covers Sweetwater's spaced-out price markup, financing figures that look like prices, discontinued pages that keep their price, and cache copies of different ages.

## Skills

| Skill | Does |
|---|---|
| `sweetwater-fetch-route` | The bot wall, the Exa-cache route, item-ID URL tricks, what counts as a live check |
| `sweetwater-listing-check` | Price, stock text, item ID, cable/bundle contents, Certified Open Box and Gear Exchange offers |
| `sweetwater-search` | Exa queries, category and brand URLs, reading category rows and deal counts |
| `sweetwater-international` | Item-by-item export limits, who to ask, comparing against a dealer that ships abroad |

## Command

- `/sweetwater:sweetwater-check <URL | item ID | model>...`

## Scripts

- `scripts/parse_exa_sweetwater.py`: Exa markdown to JSON. It strips financing, normalises `$ 239 .00`, and handles discontinued and special-order pages. A sample is in `tests/`.
- `scripts/sweetwater-extract.js`: in-browser extractor for a page that does load live. It has not been tested on a live page yet. Contributions from a US connection are welcome.

## Requirements

An Exa MCP server (search and fetch).

## Related plugins

- [`shopping`](https://github.com/danielrosehill/Claude-Shopping-Plugin): the general plugin. Its `marketplace-plugins` skill is the roster.
- [`bh-photo`](https://github.com/danielrosehill/BH-Photo-Plugin): B&H Photo, which can be read live and ships internationally.
- [`amazon`](https://github.com/danielrosehill/Claude-Amazon-Plugin), [`procurement-tools`](https://github.com/danielrosehill/procurement-tools-plugin).

## Install

```bash
claude plugins marketplace add danielrosehill/Claude-Code-Plugins
claude plugins install sweetwater@danielrosehill
```

MIT licence.
