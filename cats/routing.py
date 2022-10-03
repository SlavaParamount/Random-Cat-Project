from django.urls import path

from .consumers import PicsConsumer

ws_urlpatterns = [
    path('ws/pics/', PicsConsumer.as_asgi()),
]