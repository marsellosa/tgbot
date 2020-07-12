from django.shortcuts import render

def inicio_view(request):
    page_name = "apps/main/inicio.html"
    # msg = request.user.first_name if request.user.is_authenticated() else ''
    title = 'Inicio'
    context = {}
    return render(request, page_name, context)
