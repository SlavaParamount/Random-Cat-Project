from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PicsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.channel_layer.group_add('cats', self.channel_name)
        await self.accept()
        
    async def disconnect(self, code):
        print("disconnected")
        await self.channel_layer.group_discard('cats', self.channel_name)
    
    async def send_new_data(self, event):
        print("sending data")
        new_data = event['text']
        await self.send(json.dumps(new_data))