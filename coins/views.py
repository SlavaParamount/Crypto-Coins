from django.shortcuts import render
import requests

def index(request):
    url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    coins=requests.get(url).json()
    return render(request, 'index.html', context={'coins': coins})