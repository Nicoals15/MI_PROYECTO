from django.urls import path
from .views import (
    ProcesarCorreosAPIView,
    CorreoListAPIView,
    CorreoDetailAPIView,
    CorreoListAPIView,
    CorreoCreateAPIView
)

urlpatterns = [
    path('procesar/', ProcesarCorreosAPIView.as_view()),
    path('', CorreoListAPIView.as_view()),
    path('<int:pk>/', CorreoDetailAPIView.as_view()),
    path("", CorreoListAPIView.as_view(), name="correo-listar"),
    path("crear/", CorreoCreateAPIView.as_view(), name="correo-crear"),
]
