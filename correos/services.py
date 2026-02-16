import yaml
from pathlib import Path
from django.conf import settings
from .models import Correo

PALABRAS_CLAVE = {
    'pqr': ['inconforme', 'error', 'insatisfecho', 'pqr'],
    'demanda': ['demanda', 'litigio', 'juicio'],
    'tutela': ['tutela', 'acción de tutela', 'solicitud de tutela']
}


def buscar_categoria(texto: str):
    texto = texto.lower()
    for categoria, palabras in PALABRAS_CLAVE.items():
        for palabra in palabras:
            if palabra in texto:
                return categoria
    return 'ninguno'

def clasificar_correo(asunto: str, cuerpo: str) -> str:
    texto = f"{asunto} {cuerpo}"
    return buscar_categoria(texto)



def procesar_correos_desde_yaml(ruta_yaml='correos/data/correos.yaml'):
    ruta_absoluta = Path(settings.BASE_DIR) / ruta_yaml

    with open(ruta_absoluta, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    for correo in data.get('correos', []):
        cuerpo = correo.get('body', '')
        asunto = correo.get('subject', '')

        categoria = buscar_categoria(asunto + ' ' + cuerpo)

        Correo.objects.update_or_create(
            correo_id=correo['id'],
            defaults={
                'asunto': asunto,
                'cuerpo': cuerpo,
                'categoria': categoria
            }
        )
