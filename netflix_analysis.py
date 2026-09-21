# Netflix Data Analytics Project
# End-to-end analysis: cleaning, EDA, KPIs, visualizations and export
# Dataset: Netflix Movies and TV Shows (Kaggle)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("netflix_movies (1).csv")

# 2. Inspect
print(df.shape)
print(df.info())
print(df.isna().sum())
print("Duplicates:", df.duplicated().sum())

# 3. Clean
for col in ["type", "title", "director", "cast", "country", "rating", "duration", "listed_in"]:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Explicitly label missing categorical analysis fields
for col in ["director", "cast", "country", "rating", "duration"]:
    df[col] = df[col].fillna("Unknown")

# 4. Feature engineering
df["date_added_year"] = df["date_added"].dt.year
df["date_added_month"] = df["date_added"].dt.month
df["duration_value"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)")[0], errors="coerce"
)
df["duration_unit"] = df["duration"].str.extract(r"(min|Season|Seasons)")[0]
df["listed_in_primary"] = df["listed_in"].str.split(",").str[0].str.strip()
df["country_primary"] = df["country"].str.split(",").str[0].str.strip()

# 5. KPIs
print("Total titles:", len(df))
print("Movies:", (df["type"] == "Movie").sum())
print("TV Shows:", (df["type"] == "TV Show").sum())
print("Unique countries:", df.loc[df["country"] != "Unknown", "country_primary"].nunique())

# 6. EDA
print(df["type"].value_counts())
print(df["rating"].value_counts().head(10))
print(df["listed_in_primary"].value_counts().head(10))
print(df["country_primary"].value_counts().head(10))

# 7. Visualizations
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.savefig("movies_vs_tv_shows.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 5))
df["release_year"].value_counts().sort_index().plot(kind="line")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("titles_by_release_year.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 6))
df["listed_in_primary"].value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Primary Genres")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig("top_genres.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 6))
df["country_primary"].replace("Unknown", np.nan).value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Countries")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig("top_countries.png", dpi=150)
plt.show()

# 8. Export cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("Saved netflix_cleaned.csv")
