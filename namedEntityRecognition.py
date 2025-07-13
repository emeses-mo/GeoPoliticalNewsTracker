import pandas as pd
from pathlib import Path
import spacy
from spacy.lang.en.examples import sentences 


df = pd.read_csv("data/cleaned/articles_sentiment.csv")
#columns = list(df.columns.values)
#combining title plus desc
df["Combined"]= df["title"]+" "+df["description"]
df["Combined"] = df["Combined"].fillna("")
#print(df["Combined"][1])

nlp = spacy.load("en_core_web_sm")
entities = []
for cmbtext in df["Combined"]:
    doc = nlp(cmbtext)
    artEnts=[]
    for ent in doc.ents:
        if ent.label_ in ["PERSON","ORG","GPE"]:
            artEnts.append(ent.text)
    entities.append(artEnts)


df["Named_Entities"] = entities
print(df[["title", "Named_Entities"]].head(3))


df.to_csv("data/cleaned/articles_with_entites.csv",index=False)
print("CSV saved")