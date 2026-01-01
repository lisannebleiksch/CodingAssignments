"""
GDP and Inequality Data Analysis
================================
This script analyzes the relationship between GDP per capita and income inequality (Gini index).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.parent  # Go up to "5. GDP" folder

# =============================================================================
# Task 1: Load the data
# =============================================================================
print("Task 1: Loading data...")

df_gdp = pd.read_csv(SCRIPT_DIR / "gdp-per-capita-maddison-2020.csv")
df_gini = pd.read_csv(SCRIPT_DIR / "economic-inequality-gini-index.csv")

print("\nGDP dataset preview:")
print(df_gdp.head())
print(f"\nGDP dataset shape: {df_gdp.shape}")

print("\nGini dataset preview:")
print(df_gini.head())
print(f"\nGini dataset shape: {df_gini.shape}")

# =============================================================================
# Task 2: Clean the GDP dataset
# =============================================================================
print("\n" + "="*50)
print("Task 2: Cleaning GDP dataset...")

# Drop unnecessary columns (the annotations column)
df_gdp = df_gdp.drop(columns=["417485-annotations"])

print("\nGDP columns after cleaning:")
print(df_gdp.columns.tolist())

# =============================================================================
# Task 3: Convert Year to datetime
# =============================================================================
print("\n" + "="*50)
print("Task 3: Converting Year to datetime...")

# Filter out invalid years (must be 4 digits, between 1800-2100)
df_gdp = df_gdp[df_gdp["Year"].between(1800, 2100)]
df_gini = df_gini[df_gini["Year"].between(1800, 2100)]

df_gdp["Year"] = pd.to_datetime(df_gdp["Year"], format="%Y")
df_gini["Year"] = pd.to_datetime(df_gini["Year"], format="%Y")

print(f"\nGDP Year dtype: {df_gdp['Year'].dtype}")
print(f"Gini Year dtype: {df_gini['Year'].dtype}")

# =============================================================================
# Task 4: Clean the Gini dataset
# =============================================================================
print("\n" + "="*50)
print("Task 4: Cleaning Gini dataset...")

# The Gini dataset looks clean, but let's verify columns
print("\nGini columns:")
print(df_gini.columns.tolist())

# Filter to Year > 1980 for better data quality
df_gdp = df_gdp[df_gdp["Year"] > "1980"]
df_gini = df_gini[df_gini["Year"] > "1980"]

print(f"\nRows in GDP after filtering Year > 1980: {len(df_gdp)}")
print(f"Rows in Gini after filtering Year > 1980: {len(df_gini)}")

# =============================================================================
# Task 5: Merge the datasets
# =============================================================================
print("\n" + "="*50)
print("Task 5: Merging datasets...")

df_merged = pd.merge(df_gdp, df_gini, on=["Entity", "Year"], how="inner")

print(f"\nRows after merging: {len(df_merged)}")
print("\nMerged dataset preview:")
print(df_merged.head())

# =============================================================================
# Task 6: Rename columns
# =============================================================================
print("\n" + "="*50)
print("Task 6: Renaming columns...")

df_merged = df_merged.rename(columns={
    "GDP per capita": "GDP",
    "Gini index": "Gini_index",
    "Code_x": "Code"
})

# Drop duplicate Code column
if "Code_y" in df_merged.columns:
    df_merged = df_merged.drop(columns=["Code_y"])

print("\nFinal columns:")
print(df_merged.columns.tolist())
print("\nFinal dataset preview:")
print(df_merged.head())

# =============================================================================
# Task 7: Calculate correlation
# =============================================================================
print("\n" + "="*50)
print("Task 7: Calculating correlation...")

# Create DataFrame with just numeric columns
df_numeric = df_merged[["GDP", "Gini_index"]].dropna()

print(f"\nRows with complete data: {len(df_numeric)}")

# Calculate correlation
correlation = df_numeric["GDP"].corr(df_numeric["Gini_index"])
print(f"\nCorrelation between GDP and Gini index: {correlation:.4f}")

# Interpretation
if correlation > 0:
    direction = "positive"
else:
    direction = "negative"

strength = abs(correlation)
if strength < 0.3:
    strength_desc = "weak"
elif strength < 0.7:
    strength_desc = "moderate"
else:
    strength_desc = "strong"

print(f"\nInterpretation: There is a {strength_desc} {direction} correlation between GDP per capita and inequality.")

# =============================================================================
# Optional: Scatter Plot
# =============================================================================
print("\n" + "="*50)
print("Optional: Creating scatter plot...")

plt.figure(figsize=(10, 6))
plt.scatter(df_numeric["GDP"], df_numeric["Gini_index"], alpha=0.5, s=10)
plt.xlabel("GDP per capita")
plt.ylabel("Gini Index")
plt.title(f"GDP per Capita vs Gini Index\nCorrelation: {correlation:.4f}")
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df_numeric["GDP"], df_numeric["Gini_index"], 1)
p = np.poly1d(z)
x_line = [df_numeric["GDP"].min(), df_numeric["GDP"].max()]
plt.plot(x_line, p(x_line), "r--", linewidth=2, label="Trend line")
plt.legend()

plt.tight_layout()
plt.savefig("gdp_vs_gini_scatter.png", dpi=150)
print("Scatter plot saved as 'gdp_vs_gini_scatter.png'")
plt.show()

# =============================================================================
# Summary
# =============================================================================
print("\n" + "="*50)
print("SUMMARY")
print("="*50)
print(f"Rows after filtering Year > 1980: {len(df_gdp)} (GDP), {len(df_gini)} (Gini)")
print(f"Rows after merging: {len(df_merged)}")
print(f"Correlation: {correlation:.4f}")
