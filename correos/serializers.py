from rest_framework import serializers
from .models import Correo
from .services import clasificar_correo


class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = "__all__"


class CorreoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ["asunto", "cuerpo"]

    def create(self, validated_data):
        asunto = validated_data["asunto"]
        cuerpo = validated_data["cuerpo"]

        categoria = clasificar_correo(asunto, cuerpo)

        return Correo.objects.create(
            asunto=asunto,
            cuerpo=cuerpo,
            categoria=categoria
        )
