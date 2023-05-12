# News Aggregator:
# Create a script that aggregates news articles from multiple sources using APIs and displays them in a unified format.

import requests


def get_news():
    sources = ["bbc-news", "cnn", "the-new-york-times"]
    api_key = "YOUR_API_KEY" # you must enter your api key here
    articles = []

    for source in sources:
        url = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + api_key # you must enter your api key here
        response = requests.get(url)
        data = response.json()
        articles.extend(data['articles'])

    for article in articles:
        print(article['title'])
        print(article['description'])
        print(article['url'])
        print("\n")


get_news()
