from django.urls import path
from .views import UpdateBot, update_db_view

urlpatterns = [
    path('', UpdateBot.as_view(), name='update'),
    path('update/', update_db_view, name='update_db'),
]
