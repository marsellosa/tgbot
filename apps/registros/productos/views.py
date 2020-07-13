from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def update_db_view(request):
    page_name = 'apps/registros/productos/update.html'
    context = {}

    return render(request, page_name, context)