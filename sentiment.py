import pandas as pd
from textblob import TextBlob
from pathlib import Path

df = pd.read_csv("data/cleaned/articles_cleaned.csv")

def get_text(row):
    title = str(row.get("title",""))
    desc = str(row.get("description",""))
    return f"{title}. {desc}"

df["full_text"] = df.apply(get_text,axis=1)

def analyze(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0.1:
        label = "positive"
    elif score < -0.1:
        label  = "negative"
    else:
        label="neutral"
    return pd.Series([score, label])

df[["sentiment_score","sentiment_label"]] =  df["full_text"].apply(analyze)

df.drop(columns=["full_text"], inplace=True)

opfile = Path("data/cleaned/articles_sentiment.csv")
df.to_csv(opfile,index=False)

print(f"✅ Added sentiment to {len(df)} articles")
print(f"📁 Saved to {opfile}")