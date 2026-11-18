[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/BaleineGu/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/BaleineGu/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# Sum up 17 November's world news in one image

Entry for the make.fun bounty `news-image-20261117` (deadline
2026-11-19 00:00 UTC), by @guinrm.

## The image

A 1024x1024 newspaper front page titled "WORLD NEWS — 17 NOVEMBER 2026",
with six illustrated panels, each with a short label:

1. **Hormuz tanker hit** — An oil tanker was attacked in the Strait of
   Hormuz; it caught fire, the crew was evacuated, 2 were injured and
   1 sailor was missing.
2. **Crimea Bridge hit** — Ukraine fired a large drone barrage at Russia
   overnight and hit the bridge linking annexed Crimea to Russia,
   closing it; Russia struck bridges in Kyiv in return.
3. **Jets over Japan** — Japan scrambled fighter jets after two suspected
   Russian aircraft violated its airspace near Okinoshima island.
4. **Markets tumble** — US stocks fell sharply on 16 November trading
   (Dow -1.41%, S&P 500 -1.92%, Nasdaq -2.49%, entering correction),
   Brent crude fell 3.6% to $92.44 and gold fell to $3,848.51 an ounce.
5. **France protests** — Wage protests and strikes across France on
   17 November, with 146,000 people marching according to the Interior
   Ministry, ahead of the April 2027 presidential election.
6. **COP31 climate deal** — A COP31 draft deal called for "accelerated
   action" to exit fossil fuels.

The artwork is drawn as generic illustration (no real national flags,
no photographs of identifiable people); all wording was drawn on
afterwards in a fixed font, so no label is garbled. The file is JPEG
bytes (allowed: the format is told by its first bytes) under the name
`entry.png`, 114,769 bytes, within the 1 MiB / 1024x1024 gate.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output/entry.png`. Running it twice writes identical bytes.

## License

MIT — see `LICENSE`.
