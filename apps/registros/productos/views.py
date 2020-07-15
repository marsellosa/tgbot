import csv, io
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Categoria

@staff_member_required
def update_db_view(request):
    page_name = 'apps/registros/productos/update.html'
    context = {
        'msg':'Lista cargada exitosamente'
    }

    if request.method == 'GET':
        context = {
            'msg':'Solo Archivos *.CSV'
        }
        return render(request, page_name, context)

    csv_file = request.FILES['file']
    file = io.TextIOWrapper(csv_file)
    reader = csv.DictReader(file)

    for row in reader:
        Categoria.objects.update_or_create(
            nombre = str(row['nombre']),
            defaults={
                'descripcion' : str(row['descripcion']),
                'cantidad' : int(row['cantidad']),
                'puntos_volumen' : float(row['puntos_volumen']),
                'distribuidor' : float(row['distribuidor']),
                'consultor_mayor' : float(row['consultor_mayor']),
                'productor_calificado' : float(row['productor_calificado']),
                'mayorista' : float(row['mayorista']),
                'cliente_bs' : float(row['cliente_bs']),
                'cliente_sus' : float(row['cliente_sus'])
            }
            
        )

    return render(request, page_name, context)