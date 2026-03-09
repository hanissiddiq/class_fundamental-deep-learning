import pandas as pd
import re

print("Membaca dataset...")
data = pd.read_csv("dataset_review.csv")

def label_sentimen(score):
    if score >= 4:
        return "positif"
    elif score == 3:
        return "netral"
    else:
        return "negatif"

data["sentiment"] = data["score"].apply(label_sentimen)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

data["clean"] = data["content"].apply(clean_text)

data.to_csv("dataset_clean.csv", index=False)

print("Preprocessing selesai.")
print(data.head())