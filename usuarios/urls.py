from django.urls import path
from .views import lista_usuarios

urlpatterns = [
    path('', lista_usuarios),
]
