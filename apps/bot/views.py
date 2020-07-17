# import os
from django.shortcuts import render
from decouple import config
from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import User
from ..registros.productos.models import Categoria

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
    key = ReplyKeyboardMarkup(row_width=cols, resize_keyboard=True, one_time_keyboard=True)
    queryset = Categoria.objects.filter(activo=True)
    nro_items = queryset.count()
    vueltas = int(nro_items//cols)
    impar = True if nro_items%cols > 0 else False

    i = 0
    for _ in range(vueltas):
        btn_izq = str(queryset[i])
        i += 1
        btn_der = str(queryset[i])
        i += 1
        key.row(btn_izq, btn_der)

    if impar:
        key.row(str(queryset[i]))

    msg = "Esta es la lista de productos que tengo de Bolivia"
    bot.send_message(message.chat.id, msg, reply_markup=key)

@bot.message_handler(content_types='text')
def send_Message(message):
    tc = 6.96
    user_id = message.chat.id
    nombre = message.chat.first_name if not None else '!'
    msg = f'Hola {nombre}!, usa el link /ayuda, para tener mas información'

    if not User.objects.filter(user_id=user_id).exists():
        user = User()        
        user.user_id = message.chat.id
        user.first_name = message.chat.first_name
        user.last_name = message.chat.last_name
        user.username = message.chat.username
        user.save()

        
    text = message.text
    # new_member = message.new_chat_members
    # print(message)
    # msg = text
    try:
        producto = Categoria.objects.get(nombre__iexact=text, activo=True)
        dist = float(producto.distribuidor) * tc
        cons = float(producto.consultor_mayor) * tc
        prod = float(producto.productor_calificado) * tc
        mayo = float(producto.mayorista) * tc
        msg = f"""{producto.descripcion}:\nCantidad: {producto.cantidad}\nPV: {producto.puntos_volumen}\n25%: {producto.distribuidor} $us | {dist:5.1f} Bs.\n35%: {producto.consultor_mayor} $us | {cons:5.1f} Bs.\n42%: {producto.productor_calificado} $us | {prod:5.1f} Bs.\n50%: {producto.mayorista} $us | {mayo:5.1f} Bs.\nCliente:\n$us: {producto.cliente_sus} | Bs: {producto.cliente_bs}"""
    except:
        pass
        
    bot.send_message(message.chat.id, msg)


    