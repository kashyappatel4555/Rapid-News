from django.shortcuts import render
import requests

def index(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category='
    response = requests.get(url=url)
    news_data = response.json()
    records['allnews'] = news_data
    return render(request, 'index.html', records)


def sports(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=sports'
    response = requests.get(url=url)
    sports_news = response.json()
    records['sportsnews'] = sports_news
    return render(request, 'sports.html', records)


def entertainment(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=entertainment'
    response = requests.get(url=url)
    entertainment_news = response.json()
    records['entertainmentnews'] = entertainment_news
    return render(request, 'entertainment.html', records)

def technology(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=technology'
    response = requests.get(url=url)
    tech_news = response.json()
    records['technews'] = tech_news
    return render(request, 'technology.html', records)


def science(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=science'
    response = requests.get(url=url)
    science_news = response.json()
    records['sciencenews'] = science_news
    return render(request, 'science.html', records)


def politics(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=politics'
    response = requests.get(url=url)
    politics_data = response.json()
    records['politicsnews'] = politics_data
    return render(request, 'politics.html', records)


def national(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=national'
    response = requests.get(url=url)
    national_data = response.json()
    records['nationalnews'] = national_data
    return render(request, 'national.html', records)


def world(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=world'
    response = requests.get(url=url)
    world_data = response.json()
    records['worldnews'] = world_data
    return render(request, 'world.html', records)


def automobile(request):
    records = {}
    url = 'https://inshorts.deta.dev/news?category=automobile'
    response = requests.get(url=url)
    automobile_data = response.json()
    records['automobilenews'] = automobile_data
    return render(request, 'automobile.html', records)