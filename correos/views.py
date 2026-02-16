from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Correo
from .services import procesar_correos_desde_yaml
from .serializers import CorreoSerializer, CorreoCreateSerializer

class ProcesarCorreosAPIView(APIView):
    def get(self, request):
        procesar_correos_desde_yaml()
        return Response({"mensaje": "Correos procesados correctamente"})

class CorreoListAPIView(generics.ListAPIView):
    queryset = Correo.objects.all()
    serializer_class = CorreoSerializer


class CorreoDetailAPIView(generics.RetrieveAPIView):
    queryset = Correo.objects.all()
    serializer_class = CorreoSerializer

class CorreoCreateAPIView(generics.CreateAPIView):
    queryset = Correo.objects.all()
    serializer_class = CorreoCreateSerializer