# Week 2 - Sales Data Analysis Project
# Data Cleaning & KPI Calculations
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

# ==================================================================================
# 1. DATA ENGINEER - DATA CLEANING
# ==================================================================================

print("1. IMPORT DATASET...")
print("-" * 60)

try:
    df = pd.read_csv(DATA_FILE_PATH)
    print("Dataset imported successfully!")
    print(f"Shape: {df.shape} rows x columns)")
    print(f"Rows: {df.shape[0]:,}   Columns: {df.shape[1]}")
    print("n\nFirst 5 rows:")
    print(df.head())
    print()
except FileNotFoundError:
    print(f"ERROR: File not found - {DATA_FILE_PATH}")
    print("Please check the path and try again.")
    exit(1)
except Exception as e:
    print(f"ERROR reading file: {e}")
    exit(1)

# ─────────────────────────────────────────────────────────────
# 2. INITIAL DATA EXPLORATION
# ─────────────────────────────────────────────────────────────
print("\n2. INITIAL DATA EXPLORATION")
print("-" * 60)

print("Column information:")
print(df.info())
print()

print("Statistical summary (numeric columns):")
print(df.describe())
print()

print("Unique values - key categorical columns:")
print(f"Products: {df['Products'].unique()}")
print(f"Regions: {df['Region'].unique()}")
print(f"Sales Reps: {sorted(df['Sales_Rep'].unique())}")
print(f"Unique Order IDs: {df['Order_ID'].nunique():,}")

# ─────────────────────────────────────────────────────────────
# 3. DATA QUALITY CHECKS
# ─────────────────────────────────────────────────────────────
print("\n3. DATA QUALITY CHECKS")
print("-" * 60)

# Checks for missing Values
print("3.1 Missing values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_report = pd.DataFrame({
    'Missing':missing,
    'Missing':missing_pct.round(2)
}).loc[lambda x: x['Missing'] > 0]

if missing_report.empty:
    print("No missing values found")
else:
    print(missing_report)
print()

# Checks for duplicates
print("3.2 Duplicates:")
dup_rows = df.duplicated().sum()
dup_orders = df['Order_ID'].duplicated().sum()
print(f"Duplicate rows: {dup_rows}")
print(f"Duplicate Order_IDs: {dup_orders}")
print("No duplicates" if dup_rows == 0 else "Duplicates found!")
print()

# Checks for Revenue Consistency
print("3.3 Revenue consistency check:")
df_temp = df.copy()
df_temp['Calc_Revenue'] = df_temp['Units_Sold'] * df_temp['Unit_Price']
discrepancies = df_temp[df_temp['Revenue'] != df_temp['Calc_Revenue']]
print(f"Revenue mismatched=s found: {len(discrepancies)}")
if len (discrepancies) > 0:
    print(discrepancies[['Order_ID', 'Unit_Price', 'Revenue', 'Calc_Revenue']])
else:
    print("All revenue values are consistent")
print()

# ─────────────────────────────────────────────────────────────
# 4. DATA CLEANING
# ─────────────────────────────────────────────────────────────
print("\n4. DATA CLEANING")
print("-" * 60)

df_clean = df.copy()

# Remove temporary column, if they exists
if 'Calc_Revenue' in df_clean.columns:
    df_clean = df_clean.drop(columns=['Calc_Revenue'])

# Convert date to correct format
print("Converting Order_Date to datetime...")
df_clean['Order_Date'] = pd.to_datetime(df_clean['Order_Date'])
print(f"→ Date type: {df_clean['Order_Date'].dtype}")
print(f"Date range: {df_clean['Order_Date'].min():%Y-%m-%d} → {df_clean['Order_Date'].max():%Y-%m-%d}")
print()

# Missing values handling (demonstration purposes – not needed in this dataset)
print("Missing value handling check:")
if df_clean.isnull().sum().sum() > 0:
    print("Handling missing values...")
else:
    print("No missing values to handle")
print()

# Duplicates removal (demonstration purposes – not needed in this dataset)
print("Duplicate removal check:")
before = len(df_clean)
df_clean = df_clean.drop_duplicates()
removed = before - len(df_clean)
print(f"Removed {removed} duplicate rows" if removed > 0 else "✓ No duplicates removed")
print()

print("Final cleaned dataset shape:", df_clean.shape)
print("First 3 rows of cleaned data:")
print(df_clean.head(3))
print("\n" + "="*70)
print("DATA CLEANING FINISHED")
print("="*70 + "\n")

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
# 1. TOTAL REVENUE
# ─────────────────────────────────────────────────────────────
print("KPI 1: TOTAL REVENUE")
total_revenue = df_analysis['Revenue'].sum()
print(f"→ R {total_revenue:,.2f}")
print()

# ─────────────────────────────────────────────────────────────
# 2. AVERAGE UNITS SOLD PER ORDER
# ─────────────────────────────────────────────────────────────
print("KPI 2: AVERAGE UNITS SOLD PER ORDER")
avg_units = df_analysis['Units_Sold'].mean()
print(f"→ {avg_units:.2f} units")
print()

# ─────────────────────────────────────────────────────────────
# 3. REVENUE BY REGION
# ─────────────────────────────────────────────────────────────
print("KPI 3: REVENUE BY REGION")
revenue_by_region = df_analysis.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
for region, rev in revenue_by_region.items():
    print(f"  {region:18} : R {rev:,.2f}")
print()

# ─────────────────────────────────────────────────────────────
# 4. HIGHEST REVENUE SALES REPRESENTATIVE
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