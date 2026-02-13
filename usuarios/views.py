from django.shortcuts import render
from django.http import JsonResponse
from .models import usuario

def lista_usuarios(request):
    usuarios = usuario.objects.all().values()
    return JsonResponse(list(usuarios),safe=False)


