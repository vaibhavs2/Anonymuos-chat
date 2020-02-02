from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # self.room_name = "bc"
        # self.room_group_name = 'chat_%s' % self.room_name
        # # Join room group
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.accept()
        await self.send(text_data=json.dumps({
            'my_channel_key': self.channel_name
        }))

    async def disconnect(self, close_code):
        # Leave room group
        pass
    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # Send message to room group
        data = {
            'type': 'chat_message',
            'message': text_data_json['message'],
            'myChannel': self.channel_name,
        }
        if('profile_pic' in text_data_json):
            data["profile_pic"] = text_data_json['profile_pic']

        await self.channel_layer.send(
            text_data_json['channelToSend'].strip(), data)

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
