from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from apps.registros.productos.models import Categoria, Detalles
from apps.bot.models import User


@staff_member_required
def inicio_view(request):
    page_name = "apps/main/inicio.html"
    producto = Categoria.objects.get(nombre='BATIDO')
    detalles = Detalles.objects.all()
    users = User.objects.all()
    context = {
        'producto': producto,
        'detalles' : detalles,
        'users': users
    }

    return render(request, page_name, context)
