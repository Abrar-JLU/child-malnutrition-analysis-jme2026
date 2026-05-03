# Child Malnutrition Analysis — JME 2026 Edition

A regional data visualization project exploring child stunting, wasting, and the stunting gender gap across UNICEF regions from 2000 to 2024.

---

## Why I made this

I'm applying for a data internship at UNICEF's Office of Strategy and Evidence (Innocenti, Florence) and wanted to work with the actual datasets the team uses — not just list tools on a CV. The UNICEF–WHO–World Bank Joint Child Malnutrition Estimates felt like the right place to start: it's the flagship global dataset for SDG 2.2 tracking, it was just updated in March 2026, and it includes sex-disaggregated estimates for the first time ever.

I also have a background in public health nutrition and spent time working with UNICEF in Cox's Bazar, Bangladesh — so this data isn't abstract to me. I've been in the camps where some of these numbers come from.

---

## Data source

**UNICEF–WHO–World Bank Joint Child Malnutrition Estimates (JME), March 2026 Edition**  
[data.unicef.org/topic/nutrition/malnutrition](https://data.unicef.org/topic/nutrition/malnutrition/)

The dataset covers stunting, wasting, severe wasting, and overweight prevalence for children under 5, with regional and global estimates from 2000 to 2024 across 163 countries. The 2026 edition is the first to include sex-disaggregated estimates for stunting and overweight.

---

## What I looked at

**Three questions guided the analysis:**

1. How has stunting prevalence changed across UNICEF regions over the past 25 years — and are we anywhere close to the 2030 SDG target?
2. How does the picture look in 2024 when you put stunting and wasting side by side across regions?
3. Now that we finally have sex-disaggregated data — is there actually a gender gap in stunting, and how big is it?

---

## Key findings

**TL;DR:** Global stunting stalled after 2020. South Asia has the world's highest wasting rate at 14.1%. Boys are more stunted than girls in every single region — a brand new finding from JME 2026.

Honestly, a few things surprised me when I actually sat with the numbers.

The headline looks okay — global stunting dropped from 33.1% in 2000 to 23.2% in 2024. But when you look at the trend lines closely, progress has basically flatlined since 2020 in the regions that matter most. South Asia, West & Central Africa, East & Southern Africa — these three regions together hold about 75% of all stunted children in the world, and none of them are moving fast enough to hit the 2030 SDG target. We're going to miss it by a significant margin.

South Asia's wasting number caught my attention too. At 14.1% in 2024, it's not just the highest of any region — it's more than double the next highest. Stunting and wasting tend to get discussed separately in the literature, but seeing them side by side in Chart 2 makes the South Asia situation look quite different from everywhere else.

The gender finding was the one I found most interesting. Boys are more stunted than girls in every single UNICEF region — not in most regions, in all of them. The gap is biggest in West & Central Africa (34.8% boys vs 30.1% girls) and East & Southern Africa (34.5% vs 29.6%). This is the first time JME has published sex-disaggregated stunting estimates, so there isn't much analysis of this yet. I'd be curious to understand whether this reflects biological differences, feeding practices, healthcare-seeking behaviour, or something else entirely — probably a combination.

---

## Files

| File | Description |
|------|-------------|
| `Child_Malnutrition_Analysis_Siddique_2026.xlsx` | Main report with 3 charts and data tables |
| `JME_Regional_Global_Estimates_March_2026.xlsx` | Original source data from UNICEF DATA (unchanged) |
| `malnutrition_analysis.py` | Python script used to extract and filter the data |
| `stunting_trend_2000_2024.csv` | Chart 1 data output |
| `regional_snapshot_2024.csv` | Chart 2 data output |
| `gender_gap_2024.csv` | Chart 3 data output |

The Excel report includes:
- **Chart 1** — Stunting trend lines 2000–2024 for 4 UNICEF regions + global average
- **Chart 2** — Stunting vs wasting side-by-side for all 7 UNICEF regions (2024)
- **Chart 3** — Boys vs girls stunting + gap by region (2024, sex-disaggregated)
- Raw data sheets for full transparency

---

## Tools used

- Python (pandas) — loading and filtering the JME dataset, saving outputs as CSV
- Microsoft Excel — building the charts and report layout
- Data source: UNICEF DATA portal

---

## About me

I'm an M.Sc. candidate in Transition Management at Justus Liebig University Giessen, Germany, with a background in public health nutrition and data management. Before starting my degree I worked with UNICEF in Cox's Bazar as an Emergency Data Officer, managing nutrition datasets and leading the rollout of the Emergency Nutrition Information System (ENIS/ENIM).

I'm interested in child and maternal nutrition data — not just as a career direction, but as something I've been working on for most of my professional life.

📧 md.abrar.mozahid.siddique@tm.uni-giessen.de

---

*Data: UNICEF–WHO–World Bank JME, March 2026. Analysis completed May 2026.*
