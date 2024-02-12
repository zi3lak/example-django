import requests

def fetch_news(api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': api_key,
        'language': 'en',
        'q': 'cryptocurrency',  # Dodano parametr q do zapytania
        'pageSize': 12,  # liczba artykułów do pobrania
        'sortBy': 'publishedAt'  # sortowanie według daty publikacji
    }
    response = requests.get(url, params=params)
    return response.json()['articles']

