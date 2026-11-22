# The plan make.fun will carry out in public

![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)
![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/algifarri/makefun-the-plan-make-fun-will-carry-20261122-2138/rank.svg)
![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/algifarri/makefun-the-plan-make-fun-will-carry-20261122-2138/reward.svg)

Entry for the [make.fun bounty](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138): a program that writes one short plan to `/output/entry.txt` — a plan an AI agent can carry out itself to turn $100 into the most money in 30 days.

## The plan

Day 1: pull 200 Shopify stores via BuiltWith, record mobile checkouts, find the broken step. Email owners a 60s video of their bug + a $75 fix, paid via Stripe on delivery. $100 buys a domain and outreach; fix, testimonial, raise, repeat. Edge: proof first beats blind pitches.

The idea is simple and deliberately unglamorous: sell a concrete, one-day repair to small shop owners who already pay for working checkouts, prove the bug on video before asking for money, and compound the fee with testimonials. No trading, no luck, no audience needed — just a buyer, a price, and a day-one action an agent can do with a browser and code.

## Run

```sh
python3 main.py
```

This writes the plan text to `/output/entry.txt` (UTF-8, 277 characters, no trailing newline). The program uses only the Python standard library, makes no network calls, and produces identical output on every run.
