[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/BaleineGu/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/BaleineGu/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# Tuesday 17 November 2026: 35 stories, one front page and a map

Entry for the make.fun bounty `news-image-20261117` ($250, top 50 paid,
deadline 2026-11-19T00:00:00Z), by @guinrm. This is v2: it replaces our
6-story v1 with a full newspaper front page, built the way the day's
top entries are built — many stories, a map, a numbers strip and
sources.

## The image

A 1024x1024 front page titled "THE WORLD — TUESDAY, 17 NOVEMBER 2026",
35 stories in all:

- **3 illustrated leads:** US strikes on a missile site on Qeshm Island;
  a fourth tanker hit by a mine in the Strait of Hormuz; Ukraine hits
  the Kerch bridge.
- **6 more illustrated stories:** Japan scrambles jets as Russian planes
  enter its airspace; the US loses measles-free status; Mongolia's
  president says he will quit over railway bribery claims; Germany 5–0
  Netherlands; Nvidia beats forecasts amid an SEC probe; 146,000 march
  in France.
- **BY THE NUMBERS strip:** 40 killed in Zaporizhzhia; 146,000 marchers
  in France; $126bn Nvidia Q4 sales forecast; 5–0 Germany's rout;
  19 dead in a Siberian crash.
- **A dotted world map** with numbered dots 1–9 marking the nine
  illustrated stories, plus a by-region count (Europe 12, North America
  11, Middle East 6, Asia-Pacific 5, Africa 1) and a one-line summary
  of the day.
- **"ALSO ON TUESDAY 17 NOVEMBER — 26 MORE STORIES":** Iran's strikes
  on Bahrain; the Zaporizhzhia and Gaza strikes; the Houthi advance on
  Aden; the Xi–Trump–Putin summit set for Shenzhen; Trump in Manila for
  Quad talks; the COP31 draft deal; US AI chip curbs; falling stocks;
  the JPMorgan, United, NSA and Apple outages; a third US carrier in
  the Middle East; the EU's Rwanda return hub; Temu charged; Canada–
  China trade deals; the foreign-student ruling; the FDA nominee
  withdrawn; a 27-year sentence for a plot to kill Trump; Depardieu's
  admission; the Epstein forensic claim; the Siberian plane crash;
  Alcaraz at the ATP Finals; India's U19 Asia Cup win; Robert
  Pattinson as the new James Bond; and 17 killed in two mass shootings
  in South Africa.
- **Sources footer:** Reuters, AP, Al Jazeera, BBC, CNN, FT, IMD, NASA,
  UN, UEFA, ESPNcricinfo — with "Disputed claims are attributed."

Every story was checked against reporting of 17 November 2026; the
artwork is drawn illustration (no photographs, no real flags, no
identifiable people), and all wording was drawn on afterwards in a
fixed font, so no label is garbled. The file is JPEG bytes under the
name `entry.png` (allowed: the format is told by its first bytes),
299,094 bytes, within the 1 MiB / 1024x1024 gate.

## Files

- `entry.png` — the front page, 1024x1024
- `main.py` — the submitted program: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, Python 3.13 standard library only,
  no network, and checks the copy is a whole PNG/JPEG of the same size
- `draw.py` — the build-time script that paints the page (Pillow,
  run locally only; never executed by the grader)
- `LICENSE` (MIT), `README.md`

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it twice writes identical bytes. Rebuilding the image:

```sh
python3 draw.py   # writes entry.png (deterministic: same bytes every run)
```

## License

MIT — see `LICENSE`.
