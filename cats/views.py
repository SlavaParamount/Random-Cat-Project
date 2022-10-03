from urllib import response
from django.shortcuts import render
import requests

def IndexView(request):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url).json()[0]
    pic = response['url']
    print(pic)
    return render(request, "index.html", context={'img': pic})