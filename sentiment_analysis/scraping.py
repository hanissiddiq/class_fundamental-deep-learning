from google_play_scraper import reviews, Sort
import pandas as pd

# Ganti dengan package aplikasi lain jika diperlukan
APP_ID = "com.tokopedia.tkpd"

print("Mengambil data review dari Google Play...")

result, continuation_token = reviews(
    APP_ID,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=3000
)

data = pd.DataFrame(result)[['content','score']]

data.to_csv("dataset_review.csv", index=False)

print("Scraping selesai.")
print("Jumlah data:", len(data))