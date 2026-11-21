---
license: cc-by-4.0
pretty_name: Tally — company and open-source numbers with history and sources
language: [en]
size_categories: [10K<n<100K]
tags: [finance, startups, valuation, funding, open-source, time-series, github, npm, pypi]
configs:
  - config_name: numbers
    data_files: numbers.csv
  - config_name: history
    data_files: history.csv
---

# Tally: numbers about companies and open-source projects, each with its history and source

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24429662.svg)](https://doi.org/10.5281/zenodo.24429662)

A snapshot of the public record kept at [tallycatalog.com](https://tallycatalog.com): 788 numbers about 229 companies and
open-source projects, with 51,697 dated values going back to 2005. Every value carries the address of the page it was read from.

Typical numbers: latest valuation, total funding raised, quarterly and annual revenue, plan and API prices, headcount,
open roles, GitHub stars, weekly npm and PyPI downloads, Y Combinator batch sizes.

Snapshot date: 2026-11-21. The live record changes daily; the current files are always at
<https://tallycatalog.com/data/numbers.csv> and <https://tallycatalog.com/data/history.csv>.

## Files

### `numbers.csv` — one row per number

| column | meaning |
|---|---|
| `id` | the number's id on Tally |
| `title` | what the number is, for example `Anthropic · latest valuation` |
| `subject` | the company or project it is about |
| `unit` | `USD`, `stars`, `downloads`, `employees`, `USD/mo`, … |
| `value` | the current value |
| `as_of` | the date the current value holds for |
| `source` | the page the current value was read from |
| `history_points` | how many dated values `history.csv` has for it |
| `first_date` | the earliest dated value |
| `page` | the number's page on Tally, with its chart and the recipe for obtaining it |

### `history.csv` — one row per dated value

| column | meaning |
|---|---|
| `number_id` | matches `id` in `numbers.csv` |
| `title` | the number's title, repeated for convenience |
| `date` | the date the value holds for |
| `value` | the value on that date |
| `unit` | the unit |
| `kind` | how the value was obtained (see below) |
| `source` | the page it was read from |

`kind` is one of:

- `from the source's records` — a past value the source itself publishes (a filing, a dated announcement, a package registry's download log).
- `read by Tally` — a value Tally read from the source on that date.
- `computed from entry dates` — a count rebuilt from dated entries on the source (for example, launches per quarter from a changelog).

## How the numbers are obtained

Each number has a written recipe: which page to read, what to take from it, and how to check it. A value is recorded only
when it can be quoted from the source; Tally does not estimate. The recipe for any number is at
`https://tallycatalog.com/n/<id>/recipe`.

## Limits

- Private-company figures (valuation, revenue, funding) come from filings where they exist and otherwise from press
  reports and company announcements. They are reported figures, not audited ones.
- Coverage follows public interest: AI companies and developer tools are covered most heavily.
- 24 numbers have no source address on the current value; their history rows carry the sources.

- Values whose source allows a link and a quotation but not redistribution (company databases and aggregators) are shown on the live site and left out of these files. The numbers that depend on them are being moved to the original announcements.
- A publisher's own estimates (modelled revenue, market-implied valuations) are not recorded at all.

## Use and credit

Tally's own work is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): the compilation, its structure, and the labels and notes
Tally writes. Use it freely, with a link back. Tally claims no rights in the facts themselves (a price, a count, an announced amount): nobody
owns those. Every row names the page its value was reported on.

Suggested credit:

> Tally, https://tallycatalog.com — and for a single number, its page address from the `page` column.

Corrections and removals are logged at <https://tallycatalog.com/corrections>; to report a wrong value, open an issue at
<https://github.com/verkyyi/tally/issues>. Changes between releases of this dataset are in `CHANGES.md`.

For one number at a time, as JSON, Markdown or CSV, or its value on a past date, see <https://tallycatalog.com/llms.txt>.

## Cite

Tally. *Tally: company and open-source numbers with history and sources.* Zenodo. https://doi.org/10.5281/zenodo.24429662 (all versions; each release has its own DOI on that page).
