import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
import pickle

print("Membaca dataset...")
data = pd.read_csv("dataset_clean.csv")

# Menghapus data kosong
data = data.dropna(subset=["clean","sentiment"])

# Pastikan bertipe string
X_text = data["clean"].astype(str)
y = data["sentiment"]

tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

X = tfidf.fit_transform(X_text)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

model = LinearSVC()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Akurasi:", accuracy)
print(classification_report(y_test, y_pred))

# simpan model
with open("model_sentiment.pkl", "wb") as f:
    pickle.dump(model, f)

with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("Model berhasil disimpan")