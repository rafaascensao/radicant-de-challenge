import os
import sqlite3

import pandas as pd
import peewee as pw

from src.models.UserPreferences import UserPreferences

if os.path.exists("db/radicant_challenge.db"):
    os.remove("db/radicant_challenge.db")

df = pd.read_csv("data/ETFs.csv")

# Add the dominant sector column and remove all the sectors column
fund_sectors_col = [col for col in df if col.startswith('fund_sector')]
df["dominant_sector"] = df[fund_sectors_col].idxmax(axis=1).str.replace("fund_sector_", "")
df["dominant_sector_percentage"] = df[fund_sectors_col].max(axis=1)

# Remove columns with more than 50% of NaN values
percent_missing = df.isnull().sum() * 100 / len(df)
cols_to_drop = list(percent_missing[percent_missing > 50].index)
df = df.drop(columns=cols_to_drop)

# Remove redudant columns
df = df.drop(columns=["fund_short_name", "exchange_name"])

# Remove columns that I deemed not useful
filter_col = [col for col in df if 
                col.startswith('asset_') or 
                col.startswith('fund_price_') or 
                col.startswith('week52') or 
                col == "investment_strategy" or 
                col.startswith('category_') or
                col.startswith("years_")
            ]
df = df.drop(columns=filter_col)
df["size_type"] = df["size_type"].str.lower()

# Connect to sqlite database and save dataframe
conn = sqlite3.connect('db/radicant_challenge.db')
df.to_sql("esgfund", conn, if_exists='replace', index = False) 
conn.close()

# Create User Preferences table
psql_db = pw.SqliteDatabase('db/radicant_challenge.db')
psql_db.connect()
psql_db.create_tables([UserPreferences], safe=True)

