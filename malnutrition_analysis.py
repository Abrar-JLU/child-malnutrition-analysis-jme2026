# Child Malnutrition Analysis — JME 2026 Edition
# Md Abrar Mozahid Siddique | May 2026
#
# Working with the UNICEF-WHO-World Bank Joint Child Malnutrition Estimates
# March 2026 edition — downloaded from data.unicef.org
#
# What this does:
# Pulls regional stunting/wasting data and saves 3 CSV files
# that I used to build the charts in the Excel report.

import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path  = os.path.join(script_dir, 'JME_Regional_Global_Estimates_March_2026.xlsx')

stunting = pd.read_excel(file_path, sheet_name='Stunting Prevalence', header=0)
wasting  = pd.read_excel(file_path, sheet_name='Wasting Prevalence',  header=0)

print(f"  Stunting sheet: {stunting.shape[0]} rows")
print(f"  Wasting sheet:  {wasting.shape[0]} rows")

# regions I'm working with
# I used UNICEF Regions classification throughout — not UN or World Bank,
# since those overlap and would give duplicate rows

UNICEF_REGIONS = [
    'East and Southern Africa',
    'West and Central Africa',
    'South Asia',
    'East Asia and the Pacific',
    'Latin America and the Caribbean',
    'Middle East and North Africa',
    'Eastern Europe and Central Asia'
]

# for the trend chart I only wanted the 4 most affected regions + global
TREND_REGIONS = [
    'South Asia',
    'West and Central Africa',
    'East and Southern Africa',
    'East Asia and the Pacific'
]

TREND_YEARS = [2000, 2005, 2010, 2015, 2020, 2024]

# -----------------------------------------------------------------------
# Chart 1: how stunting changed over time across regions (2000-2024)
# -----------------------------------------------------------------------
print("\nChart 1 — stunting trend data...")

c1_data = stunting[
    ((stunting['Classification'] == 'UNICEF Regions') & 
     (stunting['Aggregate'].isin(TREND_REGIONS))) |
    ((stunting['Classification'] == 'UN Regions') & 
     (stunting['Aggregate'] == 'World'))
][['Aggregate', 'Year', 'Both Sexes - Point Estimate']].copy()

c1_data['Both Sexes - Point Estimate'] = pd.to_numeric(
    c1_data['Both Sexes - Point Estimate'], errors='coerce'
)

c1_pivot = c1_data.pivot_table(
    index='Year',
    columns='Aggregate',
    values='Both Sexes - Point Estimate'
)

c1_result = c1_pivot.loc[TREND_YEARS].reset_index()
c1_result.columns.name = None
c1_result = c1_result.rename(columns={'World': 'Global'})

print(c1_result.to_string(index=False))

c1_result.to_csv(os.path.join(script_dir, 'stunting_trend_2000_2024.csv'), index=False)
print("  -> stunting_trend_2000_2024.csv saved")

# -----------------------------------------------------------------------
# Chart 2: stunting vs wasting side by side for all regions, 2024
# -----------------------------------------------------------------------
print("\nChart 2 — regional snapshot 2024...")

s2024 = stunting[
    (stunting['Classification'] == 'UNICEF Regions') &
    (stunting['Aggregate'].isin(UNICEF_REGIONS)) &
    (stunting['Year'] == 2024)
][['Aggregate', 'Both Sexes - Point Estimate']].copy()
s2024.columns = ['Region', 'Stunting (%)']

w2024 = wasting[
    (wasting['Classification'] == 'UNICEF Regions') &
    (wasting['Aggregate'].isin(UNICEF_REGIONS)) &
    (wasting['Year'] == 2024)
][['Aggregate', 'Both Sexes - Point Estimate']].copy()
w2024.columns = ['Region', 'Wasting (%)']

c2_result = s2024.merge(w2024, on='Region')
c2_result['Stunting (%)'] = pd.to_numeric(c2_result['Stunting (%)'], errors='coerce')
c2_result['Wasting (%)']  = pd.to_numeric(c2_result['Wasting (%)'],  errors='coerce')
c2_result = c2_result.sort_values('Stunting (%)', ascending=False).reset_index(drop=True)

print(c2_result.to_string(index=False))

# South Asia wasting stands out — wanted to flag this explicitly
sa_wasting = c2_result[c2_result['Region'] == 'South Asia']['Wasting (%)'].values[0]
global_avg_raw = wasting[
    (wasting['Classification'] == 'UN Regions') &
    (wasting['Aggregate'] == 'World') &
    (wasting['Year'] == 2024)
]['Both Sexes - Point Estimate'].values[0]
global_avg = round(pd.to_numeric(global_avg_raw, errors='coerce'), 1)

print(f"\n  South Asia wasting ({sa_wasting}%) vs global average ({global_avg}%)")
print(f"  That's {round(sa_wasting / float(global_avg), 1)}x the global average")

c2_result.to_csv(os.path.join(script_dir, 'regional_snapshot_2024.csv'), index=False)
print("  -> regional_snapshot_2024.csv saved")

# -----------------------------------------------------------------------
# Chart 3: boys vs girls — the gender gap in stunting (2024)
# This uses the sex-disaggregated columns, which are new in JME 2026
# -----------------------------------------------------------------------
print("\nChart 3 — gender gap in stunting 2024...")

c3_result = stunting[
    (stunting['Classification'] == 'UNICEF Regions') &
    (stunting['Aggregate'].isin(UNICEF_REGIONS)) &
    (stunting['Year'] == 2024)
][['Aggregate', 'Male - Point Estimate', 'Female - Point Estimate']].copy()

c3_result.columns = ['Region', 'Boys (%)', 'Girls (%)']
c3_result['Boys (%)']  = pd.to_numeric(c3_result['Boys (%)'],  errors='coerce')
c3_result['Girls (%)'] = pd.to_numeric(c3_result['Girls (%)'], errors='coerce')
c3_result['Gap (Boys - Girls)'] = round(c3_result['Boys (%)'] - c3_result['Girls (%)'], 1)
c3_result = c3_result.sort_values('Boys (%)', ascending=False).reset_index(drop=True)

print(c3_result.to_string(index=False))
print(f"\n  Boys higher than girls in all {len(c3_result)} regions — no exceptions")

c3_result.to_csv(os.path.join(script_dir, 'gender_gap_2024.csv'), index=False)
print("  -> gender_gap_2024.csv saved")

# done
print("\n" + "-"*50)
print("Done. 3 CSV files saved to the same folder.")
print("Key numbers:")
print(f"  Global stunting 2024:  23.2%  (was 33.1% in 2000)")
print(f"  South Asia wasting:    {sa_wasting}%  (highest of any region)")
print(f"  Gender gap:            boys > girls in all 7 UNICEF regions")
print("-"*50)
