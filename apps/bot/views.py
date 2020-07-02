import os

from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import User
# Create your views here.
TOKEN = os.environ.get('TOKEN')
import telebot

bot = telebot.TeleBot(TOKEN)

class UpdateBot(APIView):
    def post(self,request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['/ayuda'])
def start(message):
    msg = """
        Hola! Yo soy tu asistente, y\n
        puedo ayudarte con la lista\n
        de precios de los productos\n
        HERBALIFE NUTRITION en Bolivia.\n
        Uso:\n
        /batido\n
        /aloe\n
        /te\n
    """
    bot.send_message(message.chat.id,msg)


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

