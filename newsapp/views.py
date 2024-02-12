from django.shortcuts import render
from .news import fetch_news

def news_view(request):
    api_key = 'ed4d557f3e9647848e7a84dcab433155'  # Podmień na swój klucz API
    articles = fetch_news(api_key)
    return render(request, 'news.html', {'articles': articles})
