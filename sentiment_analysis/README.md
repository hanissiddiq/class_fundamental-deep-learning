# Sentiment Analysis Project

Project ini memenuhi kriteria:
- Scraping data minimal 3000 review
- Preprocessing dan pelabelan data
- Ekstraksi fitur menggunakan TF-IDF
- Training model Machine Learning (SVM)
- Evaluasi akurasi

## Install library

pip install -r requirements.txt

## Langkah menjalankan project

1. Scraping dataset
python scraping.py

2. Preprocessing
python preprocessing.py

3. Training model
python train_model.py

4. Test prediksi
python predict.py

Dataset akan disimpan sebagai:
dataset_review.csv
dataset_clean.csv

Model tersimpan:
model_sentiment.pkl