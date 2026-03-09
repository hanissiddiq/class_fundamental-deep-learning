import pickle

model = pickle.load(open("model_sentiment.pkl","rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl","rb"))

while True:
    text = input("Masukkan kalimat: ")
    vec = tfidf.transform([text])
    pred = model.predict(vec)
    print("Sentimen:", pred[0])