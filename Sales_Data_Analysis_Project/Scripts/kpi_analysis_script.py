# Week 2 - Sales Data Analysis Project
# KPI Calculations
# 2026-01-21

import pandas as pd
import numpy as np
from datetime import datetime
import os

# ==================================================================================
# CONFIGURATION
# ==================================================================================
DATA_FILE_PATH = r"C:\Users\Lucky\Documents\GitHub\Sales-data-analysis"

OUTPUT_FOLDER = "results"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


print("=" * 70)
print(f"   SALES DATA ANALYSIS PROJECT - SCRIPT VERSION")
print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)
print()

# =============================================================
# 2. PYTHON ANALYST – KPI CALCULATIONS
# =============================================================

print("PYTHON ANALYST - KPI CALCULATIONS")
print("=" * 70)
print()

df_analysis = df_clean.copy()

# Add time dimensions
df_analysis['Order_Month'] = df_analysis['Order_Date'].dt.month
df_analysis['Order_Year']  = df_analysis['Order_Date'].dt.year
df_analysis['Month_Name']  = df_analysis['Order_Date'].dt.strftime('%B')

# ─────────────────────────────────────────────────────────────
# KPI 1. TOTAL REVENUE
# ─────────────────────────────────────────────────────────────
print("KPI 1: TOTAL REVENUE")
total_revenue = df_analysis['Revenue'].sum()
print(f"→ R {total_revenue:,.2f}")
print()

# ─────────────────────────────────────────────────────────────
# KPI 2. AVERAGE UNITS SOLD PER ORDER
# ─────────────────────────────────────────────────────────────
print("KPI 2: AVERAGE UNITS SOLD PER ORDER")
avg_units = df_analysis['Units_Sold'].mean()
print(f"→ {avg_units:.2f} units")
print()

# ─────────────────────────────────────────────────────────────
# KPI 3. REVENUE BY REGION
# ─────────────────────────────────────────────────────────────
print("KPI 3: REVENUE BY REGION")
revenue_by_region = df_analysis.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
for region, rev in revenue_by_region.items():
    print(f"  {region:18} : R {rev:,.2f}")
print()

# ─────────────────────────────────────────────────────────────
# KPI 4. HIGHEST REVENUE SALES REPRESENTATIVE
# ─────────────────────────────────────────────────────────────
print("KPI 4: HIGHEST REVENUE SALES REPRESENTATIVE")
revenue_by_rep = df_analysis.groupby('Sales_Rep')['Revenue'].sum().sort_values(ascending=False)
print("Top 5 Sales Reps:")
for i, (rep, rev) in enumerate(revenue_by_rep.head().items(), 1):
    print(f"  {i}. {rep:8} : R {rev:,.2f}")

top_rep = revenue_by_rep.index[0]
top_rep_rev = revenue_by_rep.iloc[0]
print(f"\nBest performer: {top_rep} → R {top_rep_rev:,.2f}")
print()

# ─────────────────────────────────────────────────────────────
# KPI 5. TOP 3 PRODUCTS BY UNITS SOLD
# ─────────────────────────────────────────────────────────────
print("KPI 5: TOP 3 PRODUCTS BY UNITS SOLD")
units_by_product = df_analysis.groupby('Product')['Units_Sold'].sum().sort_values(ascending=False)
top3 = units_by_product.head(3)
for i, (prod, units) in enumerate(top3.items(), 1):
    print(f"  {i}. {prod:18} : {units:,} units")
print()

# =============================================================
# EXPORT & RESULT FEEDBACK
# =============================================================

print("EXPORTING RESULTS")
print("-" * 60)

kpi_summary = pd.DataFrame({
    'KPI': [
        'Total Revenue',
        'Avg Units per Order',
        'Top Sales Rep',
        'Top Product (units)'
    ],
    'Value': [
        f"R {total_revenue:,.2f}",
        f"{avg_units:.2f}",
        top_rep,
        f"{top3.index[0]} ({top3.iloc[0]:,} units)"
    ]
})

files = {
    'kpi_summary.csv': kpi_summary,
    'revenue_by_region.csv': revenue_by_region,
    'units_by_product.csv': units_by_product
}

for filename, df_to_save in files.items():
    path = os.path.join(OUTPUT_FOLDER, filename)
    df_to_save.to_csv(path)
    print(f"→ Saved: {path}")

print("\n" + "="*70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("="*70)