from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import User
# Create your views here.

import telebot

bot = telebot.TeleBot('1075118916:AAHzfQf_rgPdS7uAiQ-Z12Az1rmjldQj9WE')

'''
https://api.telegram.org/bot1075118916:AAHzfQf_rgPdS7uAiQ-Z12Az1rmjldQj9WE/setWebhook?url=https://b5d8f52b57aa.ngrok.io/bot1075118916:AAHzfQf_rgPdS7uAiQ-Z12Az1rmjldQj9WE/

'''

class UpdateBot(APIView):
    def post(self,request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hello')


@bot.message_handler(content_types='text')
def send_Message(message):
    user_id = message.chat.id
    nombre = message.chat.first_name
    text = message.text
 
    # msg = f'Hola {nombre},\ngusto de saludarte otra vez!\n ¿Cómo puedo ayudarte?'
    msg = text

    if not User.objects.filter(user_id=user_id).exists():
        user = User()        
        user.user_id = message.chat.id
        user.first_name = message.chat.first_name
        user.last_name = message.chat.last_name
        user.username = message.chat.username
        user.save()

        msg = f'Hola {nombre}!, ¿Cómo puedo ayudarte?'

        
    bot.send_message(message.chat.id, msg)

