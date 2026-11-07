from django.shortcuts import render
from .utils import obtener_metricas_consumo, obtener_registros_consumo

def vista_panel_sustentabilidad(request):
    metricas = obtener_metricas_consumo(obtener_registros_consumo())

    return render(
        request,
        "sustentabilidad/panel.html",
        metricas
    )