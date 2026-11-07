import json
from pathlib import Path

def calcular_emisiones_carbono(consumo_kwh: int|float, factor_emision=0.4) -> int|float:
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser un valor negativo.")

    emisiones = consumo_kwh * factor_emision
    return emisiones

def obtener_metricas_consumo(registros: list[dict]) -> dict:
    emisiones_totales = 0
    planta_mayor_consumo = None
    mayor_consumo = 0

    for planta in registros:
        emisiones_totales += calcular_emisiones_carbono(planta["consumo_kwh"])

        if planta["consumo_kwh"] > mayor_consumo:
            mayor_consumo = planta["consumo_kwh"]
            planta_mayor_consumo = planta["planta"]

    return {
        "emisiones_totales": emisiones_totales,
        "planta_mayor_consumo": planta_mayor_consumo
    }

def obtener_registros_consumo() -> list:
    BASE_DIR = Path(__file__).resolve().parent
    RUTA_JSON = BASE_DIR / "registros" / "registros_plantas.json"

    with open(RUTA_JSON, "r", encoding="utf-8") as f:
        registros = json.load(f)

    return registros