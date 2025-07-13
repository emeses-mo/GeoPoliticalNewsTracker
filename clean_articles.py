import json
import pandas as pd 
from pathlib import Path

raw =  Path("data/raw")
latest = sorted(raw.glob("articles_*.json"))[-1]

with open(latest, "r", encoding="utf-8") as f:
    data =  json.load(f)

articles = data.get("articles", [])

records = []

for a in articles:
    records.append({
        "title": a.get("title"),
        "description": a.get("description"),
        "published_at": a.get("publishedAt"),
        "source": a.get("source", {}).get("name"),
        "url": a.get("url")
    })

df =  pd.DataFrame(records)

#drop rows with missing titles or dates

df.dropna(subset= ["title","published_at"],inplace =True)
opfile = Path("data/cleaned/articles_cleaned.csv")

df.to_csv(opfile,index=False)

print(f"✅ Cleaned {len(df)} articles")
print(f"📁 Saved to {opfile}")