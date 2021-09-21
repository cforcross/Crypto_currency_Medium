from django.shortcuts import render
import requests,json
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    url ="https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    res = requests.get(url)
    if res.status_code == 200:
        result = json.loads(res.content)
        return render(request, 'index.html',{"result": result})
    else:
        print(f"{url} not valid")


def fear(request):
    fear = requests.get(' https://api.alternative.me/fng/?limit=10')
    fear_api = json.loads(fear.content)

    context ={
        "fear_api":fear_api,
    }
    return render(request,'fear.html',context=context)

def price(request):
    price_array = {'BTC','ETH','USDT','ADA','BNB','XRP','SOL','USDC','DOT','DODGE'}
    test='https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR'
    fear = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms= {price_array}''MIOTA&tsyms=USD')
    price = json.loads(fear.content)

    context ={
        "price":price,
    }
    return render(request,'price.html',context=context)