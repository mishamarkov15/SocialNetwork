import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from messanger import models


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender_id']
        receiver = text_data_json['receiver_id']
        msg = models.Message(
            sender_id=models.MyUser.objects.get(id=sender),
            receiver_id=models.MyUser.objects.get(id=receiver),
            title=message[:30],
            content=message,
            status='sent',
        )
        msg.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message",
                                   "message": message,
                                   'sender_id': sender,
                                   'receiver_id': receiver}
        )

    def chat_message(self, event):
        print('chat_message')
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'sender_id': event['sender_id'],
            'receiver_id': event['receiver_id']
        }))
