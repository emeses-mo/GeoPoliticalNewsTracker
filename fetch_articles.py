import requests
import json
from datetime import datetime


API_KEY = "b6436f6bbad0432bbbe859ec97fc1039"
QUERY = "Iran OR Israel OR United States"
FROM_DATE = "2025-06-12"
SORT_BY = "publishedAt"
LANG = "en"

def fetch_articles():
    url =  "https://newsapi.org/v2/everything"
    params = {
        "q": QUERY,
        "from": FROM_DATE,
        "sortBy": SORT_BY,
        "language": LANG,
        "pageSize": 100,
        "apiKey": API_KEY,
    }

#url = "https://newsapi.org/v2/everything?q=Iran+OR+Israel+OR+United+States&from=2025-06-12&sortBy=popularity&apiKey=b6436f6bbad0432bbbe859ec97fc1039"

    response =  requests.get(url, params=params)

    if response.status_code == 200:
        data= response.json()
        print(f"✅ Fetched {len(data['articles'])} articles.")
        today = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"data/raw/articles_{today}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"📁 Saved to {filename}")
    
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_articles()
