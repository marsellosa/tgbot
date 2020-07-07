# import os
from decouple import config
from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import User
from ..registros.productos.models import Categoria
# Create your views here.
# TOKEN = config('TOKEN')
# print(TOKEN)

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(config('TOKEN'))

class UpdateBot(APIView):
    def post(self,request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['ayuda'])
def ayuda(message):
    cols = 2
    impar = False
    key = ReplyKeyboardMarkup(row_width=cols, resize_keyboard=True, one_time_keyboard=True)
    queryset = Categoria.objects.filter(activo=True)
    nro_items = queryset.count()
    vueltas = int(nro_items//cols)
    if nro_items%cols > 0:
        impar = True

    i = 0
    for _ in range(vueltas):
        btn_izq = str(queryset[i])
        i += 1
        btn_der = str(queryset[i])
        key.row(btn_izq, btn_der)
        i += 1

    if impar:
        key.row(str(queryset[i]))

    #     for _ in range(col):

    # for e in queryset:
    #     botones.append(KeyboardButton(e.nombre))
    #     a = [['**a**', 'b', 'c']]
    #     button = KeyboardButton(e.nombre)
    #     puntos = KeyboardButton(e.puntos_volumen)
    #     mayorista = KeyboardButton(e.mayorista)
    #     key.row(button)
    # key.row(botones)
    # key = ReplyKeyboardMarkup([['a', 'b', 'c']])
    
    # print(botones)
    msg = "Esta es la lista de productos que tengo de Bolivia"
    bot.send_message(message.chat.id, msg, reply_markup=key)


@bot.message_handler(commands=['batido'])
def batido(message):
    msg="""
    Batido:
    PV: 24.32
    25%: 32.30$us - 225 Bs.
    """
    bot.send_message(message.chat.id,msg)


@bot.message_handler(content_types='text')
def send_Message(message):
    user_id = message.chat.id
    nombre = message.chat.first_name if not None else '!'
    text = message.text
    msg = text
    try:
        producto = Categoria.objects.get(nombre__iexact=text)
        dist = float(producto.distribuidor) * 6.96
        msg = f"""{producto.descripcion}:\nCantidad: {producto.cantidad}\nPV: {producto.puntos_volumen}\n25%: {producto.distribuidor} $us | {dist:5.1f} Bs.\n35%: {producto.consultor_mayor} $us\n42%: {producto.productor_calificado} $us\n50%: {producto.mayorista} $us\nCliente:\nBs:"""
    except:
        pass
    
    if not User.objects.filter(user_id=user_id).exists():
        user = User()        
        user.user_id = message.chat.id
        user.first_name = message.chat.first_name
        user.last_name = message.chat.last_name
        user.username = message.chat.username
        user.save()

        msg = f'Hola {nombre}!, ¿Cómo puedo ayudarte?'

        
    bot.send_message(message.chat.id, msg)

