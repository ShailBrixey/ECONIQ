#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-23T03:25:03.277Z
"""

import pandas as pd

metadata = [
    {
        "Dataset": "Inflation Data",
        "Source": "Kaggle (FRED Data)",
        "Date Range": "1947–2023",
        "Variables": "Date, Value (in Billions)",
        "Purpose": "Track inflation trends over time for economic analysis videos.",
        "Accuracy": "High — official Federal Reserve data, updated monthly. Kaggle mirrors FRED, 1–2 month delay.",
        "Last Updated": "October 2025",
        "Source URL": "https://fred.stlouisfed.org"
    },
    {
        "Dataset": "Interest Expense on Public Debt",
        "Source": "Treasury.gov",
        "Date Range": "2010–2025",
        "Variables": "Month, Expense, Year-to-Date Expense",
        "Purpose": "Show growth of U.S. government interest expenses to highlight rising debt costs.",
        "Accuracy": "Very high — official Treasury reporting, monthly updates.",
        "Last Updated": "October 2025",
        "Source URL": "https://fiscaldata.treasury.gov/"
    },
    {
        "Dataset": "Average Treasury Interest Rates",
        "Source": "Treasury.gov",
        "Date Range": "2001–2025",
        "Variables": "Date, Average Interest Rate (%)",
        "Purpose": "Analyze relationship between interest rates and federal debt burden.",
        "Accuracy": "High — official Fiscal Data source, updated monthly.",
        "Last Updated": "October 2025",
        "Source URL": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-on-us-treasury-securities"
    },
    {
        "Dataset": "FRED Interest Payments",
        "Source": "Federal Reserve Economic Data (FRED)",
        "Date Range": "1947–2025",
        "Variables": "Date, Value (Billions), Quarter",
        "Purpose": "Examine historical changes in interest payment trends for long-term perspective.",
        "Accuracy": "High — official FRED dataset, quarterly updates.",
        "Last Updated": "October 2025",
        "Source URL": "https://fred.stlouisfed.org"
    },
    {
        "Dataset": "Government Receipts and Expenditures",
        "Source": "BEA.gov",
        "Date Range": "Varies (Quarterly, 1950–Present)",
        "Variables": "Receipts, Expenditures, GDP Components",
        "Purpose": "Provide macroeconomic context for fiscal policy and growth discussions.",
        "Accuracy": "High — official Bureau of Economic Analysis data, quarterly updates.",
        "Last Updated": "October 2025",
        "Source URL": "https://www.bea.gov/data"
    },
    {
        "Dataset": "Cumulative Federal Interest Costs",
        "Source": "pgpf.org (Peter G. Peterson Foundation)",
        "Date Range": "2019–2025",
        "Variables": "Month, Year, Value (Billions)",
        "Purpose": "Visualize recent growth in interest costs for content on fiscal sustainability.",
        "Accuracy": "Moderate — derived from Treasury data, visualization-based aggregation.",
        "Last Updated": "October 2025",
        "Source URL": "https://www.pgpf.org/chart-archive"
    },
    {
        "Dataset": "Budget and Economic Data",
        "Source": "CBO.gov (Historical Budget Data)",
        "Date Range": "1962–Present",
        "Variables": "Revenue, Debt, GDP (Billions)",
        "Purpose": "Provide long-term budgetary context for national fiscal trends.",
        "Accuracy": "High — official Congressional Budget Office data, annual updates.",
        "Last Updated": "October 2025",
        "Source URL": "https://www.cbo.gov/data/budget-economic-data"
    },
    {
        "Dataset": "Economic Projections",
        "Source": "CBO.gov",
        "Date Range": "2000–Present",
        "Variables": "Output, Prices, Labor Market, Interest Rates, Income",
        "Purpose": "Support economic forecasting for future-oriented finance videos.",
        "Accuracy": "High — official CBO projections, semiannual updates.",
        "Last Updated": "October 2025",
        "Source URL": "https://www.cbo.gov/data/budget-economic-data"
    },
    {
        "Dataset": "Demographic and Long-Term Projections",
        "Source": "CBO.gov",
        "Date Range": "2021–Present",
        "Variables": "Population, Labor Force, Potential GDP",
        "Purpose": "Support discussions on long-term fiscal sustainability and demographics.",
        "Accuracy": "High — official CBO outlook data, updated every 2 years.",
        "Last Updated": "October 2025",
        "Source URL": "https://www.cbo.gov/data/budget-economic-data"
    }
]

# Convert to DataFrame
metadata_df = pd.DataFrame(metadata)

# Display neatly
display(metadata_df)

print("Metadata sheet successfully graphed.")

metadata_df.info()
metadata_df.describe(include='all')

# Export
metadata_df.to_excel("econic_metadata_sheet.xlsx", index=False)
metadata_df.to_csv("econic_metadata_sheet.csv", index=False)

print("Metadata sheet successfully exported.")