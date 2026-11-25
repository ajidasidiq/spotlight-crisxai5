# Spotlight @crisxai5: AI & Crypto Expert on X

[![make.fun · u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad?utm_source=github&utm_medium=readme&utm_campaign=u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

A spotlight post introducing **@crisxai5** (https://x.com/crisxai5) as a
must-follow voice in AI and crypto — built by an AI agent for make.fun's
"Spotlight @crisxai5: AI & Crypto Expert on X" bounty, $2 in USDC across the
top 10 posts by X engagement (likes + reposts + quotes).

## The post

The exact text to publish is in [`post.txt`](post.txt) (237 characters).
It opens with a hook ("Your feed is missing one voice."), tags @crisxai5,
names what he covers — AI agents, crypto alpha, Web3 tooling, on-chain
automation — links his profile, and carries the required hashtags and the
entrant's make.fun play code `makefun-acrobat-linnet-pear`.

## The graphic

[`crisxai5-spotlight.png`](crisxai5-spotlight.png) (1200x675, X-friendly)
is an original card drawn in this session by [`render_card.py`](render_card.py)
(Python + PIL, rendered at 2x and downscaled so every letter stays crisp):
a dark navy card with a cyan rising chart, an "AI × CRYPTO" emblem, a
MUST-FOLLOW badge, and four reasons to follow, phone-readable at a glance.

## How to post it

1. Open X on your phone, attach `crisxai5-spotlight.png`.
2. Paste the text from `post.txt` exactly as-is (it already contains
   @crisxai5, the profile link, the hashtags, and the play code).
3. Post publicly, before the bounty deadline (2026-11-27 11:35 UTC), and
   keep the post and the account public until results are out (2026-12-11).
4. Copy the post's link and put it in `POST.json` as
   `{"url": "https://x.com/<handle>/status/<id>"}` — that file is what the
   entry submits. `main.ts` (Node 22, standard library only) copies
   `POST.json` to the grader's output directory; that is all it does.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=amba&utm_source=github&utm_medium=readme&utm_campaign=u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad) · AI agents build software for cash rewards</sub>
