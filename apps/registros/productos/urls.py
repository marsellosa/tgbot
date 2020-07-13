from django.urls import path
from .views import update_db_view

urlpatterns = [
    # path('', productos_view, name='productos'),
    path('update/', update_db_view, name='update_bd'),
]


