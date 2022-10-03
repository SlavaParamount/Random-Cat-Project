from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict


import requests
from .models import Pic

channel_layer = get_channel_layer()


@shared_task
def get_cat_url():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url).json()[0]
    url = response['url']
    
    obj, created =Pic.objects.get_or_create(uri=url)
    obj.uri = url
    print(obj)
    obj.save()
    
    pics = list(Pic.objects.all())
    
    pic_list = []
    
    for pic in pics:
        pic_list.append(model_to_dict(pic))
    
    async_to_sync(channel_layer.group_send)('cats', {'type': 'send_new_data', 'text': pic_list})