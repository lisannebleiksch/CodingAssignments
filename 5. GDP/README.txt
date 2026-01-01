# Assignment: GDP and Inequality (Data Analytics)

You will work with two real world datasets:

- **GDP per capita** (Maddison Project)
- **Income inequality** measured by the **Gini index**

Your job is to clean the data, combine the datasets and answer a simple question:

**Is there a relationship between GDP per capita and inequality?**

## What you will practice

- Loading CSV files with pandas
- Cleaning data by dropping columns and filtering rows
- Working with dates and time series columns
- Merging two datasets
- Basic statistics with correlation
- Optional: plotting a relationship with a scatter plot

## Files in this folder

You should already have these files in the repository:

- `gdp-per-capita-maddison-2020.csv`
- `economic-inequality-gini-index.csv`

If your copy of the repo does not contain them, use the GitHub raw links shown in the notebook or ask the person who shared the repo with you.

## Option A: Do it in Google Colab (recommended)

This avoids setting up a local environment.

### 1) Open Colab
Go to Google Colab and create a new notebook.

### 2) Get the files into Colab
Pick one of these options:

**Option 1: Upload**
- In Colab, click the folder icon on the left
- Click **Upload**
- Upload the two CSV files

**Option 2: Load directly from GitHub (no upload) this is prefered**
Use pandas to read the files from raw URLs. The notebook in this repo shows the exact links.

### 3) Start coding
Create code cells and follow the tasks below.

## Tasks

### Task 1: Load the data
Load the two CSV files into pandas DataFrames.

Expected result:
- `df_gdp` contains GDP per capita data
- `df_gini` contains Gini index data

Tip: use `df.head()` to sanity check the columns.

### Task 2: Clean the GDP dataset
- Drop columns you do not need
- make sure you can compare both dataframes

### Task 3: Make sure `Year` is a date column
Convert the `Year` column to a datetime type if needed.

Tip: `pd.to_datetime(...)`

### Task 4: Clean the Gini dataset
Drop columns you do not need.

### Task 5: Merge the datasets
Merge the GDP and Gini datasets on:

- `Entity`
- `Year`

Expected result:
- a combined DataFrame with both GDP and Gini columns for the same country and year

### Task 6: Rename columns
Rename columns so they are shorter and consistent, for example:

- `GDP per capita` -> `GDP`
- `Gini index` -> `Gini_index`

### Task 7: Calculate correlation
Create a DataFrame with just the two numeric columns:

- `GDP`
- `Gini_index`

Drop missing values and calculate the correlation.

Expected result:
- a number between -1 and 1
- interpret the sign and strength in one short sentence

## Optional: Plot it

### Option 1: Scatter plot
Make a scatter plot of `GDP` vs `Gini_index`.

Extra:
- add labels and a title
- optionally add a trend line (linear fit)

### Option 2: Pick one country
Filter to one `Entity` and plot how GDP and Gini change over time.

## Done checklist

You are done when you can answer these:

- How many rows are left after filtering to `Year > 1980`?
- How many rows are left after merging?
- What is the correlation between GDP per capita and the Gini index?
- Does the plot match your correlation result?


