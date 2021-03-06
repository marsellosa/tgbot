# import os
from django.shortcuts import render
from decouple import config
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Activity
from .chat import respond, welcome
from ..registros.productos.models import Categoria
from ..main.models import Settings

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(config('TOKEN'))


class UpdateBot(APIView):
    def post(self, request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


def save_new_user(message):

    from_user = message.from_user
 
    user = User()
    user.user_id = from_user.id
    user.first_name = from_user.first_name
    user.last_name = from_user.last_name
    user.username = from_user.username
    user.is_bot = from_user.is_bot
    user.language_code = from_user.language_code
    user.save()

    return User.objects.get(user_id=from_user.id)


@bot.message_handler(commands=['ayuda'])
def ayuda(message):
    start(message)


@bot.message_handler(commands=['start'])
def start(message):
    # Dibuja los botones
    cols = 2
    key = ReplyKeyboardMarkup(
        row_width=cols, resize_keyboard=True, one_time_keyboard=True)
    queryset = Categoria.objects.filter(activo=True).order_by('nombre')
    nro_items = queryset.count()
    vueltas = int(nro_items//cols)
    impar = True if nro_items % cols > 0 else False

    i = 0
    for _ in range(vueltas):
        btn_izq = str(queryset[i])
        i += 1
        btn_der = str(queryset[i])
        i += 1
        key.row(btn_izq, btn_der)

    if impar:
        key.row(str(queryset[i]))

    # Solicita un saludo segun el idioma
    msg = welcome(message)
    # 
    user_id = message.from_user.id
    # Verifica el registro
    if not User.objects.filter(user_id=user_id).exists():
        save_new_user(message)
    # Envia una respuesta
    bot.send_message(user_id, msg, reply_markup=key)


@bot.message_handler(content_types='text')
def send_message(message):
    # Verifica el registro
    try:
        user_id = User.objects.get(user_id=message.from_user.id)
    except:
        user_id = save_new_user(message)

    # Capturamos el texto solicitado por el usuario
    text = message.text

    # Registramos la actividad del usuario
    log = Activity()
    log.user = user_id
    log.text = text
    log.save()

    # calcula y envia el precio del producto solicitado
    dolar = Settings.objects.get(nombre='Dolar')
    tc = float(dolar.valor)
    
    # Procesamos la respuesta al usurio
    try:
        producto = Categoria.objects.get(nombre__iexact=text, activo=True)
        dist = float(producto.distribuidor) * tc
        cons = float(producto.consultor_mayor) * tc
        prod = float(producto.productor_calificado) * tc
        mayo = float(producto.mayorista) * tc
        msg = f"""{producto.descripcion}:\nCantidad: {producto.cantidad}\nPV: {producto.puntos_volumen}\n25%: {producto.distribuidor} $us | {dist:5.1f} Bs.\n35%: {producto.consultor_mayor} $us | {cons:5.1f} Bs.\n42%: {producto.productor_calificado} $us | {prod:5.1f} Bs.\n50%: {producto.mayorista} $us | {mayo:5.1f} Bs.\nCliente:\n$us: {producto.cliente_sus} | Bs: {producto.cliente_bs}"""
    except:
        # escoge un mensaje aleatorio
        msg = respond(message)

    # Enviamos el mensaje
    bot.send_message(user_id, msg)
