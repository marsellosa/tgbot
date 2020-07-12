from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def inicio_view(request):
    page_name = "apps/main/inicio.html"
    context = {}
    
    return render(request, page_name, context)
