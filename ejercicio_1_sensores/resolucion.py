import json
from pathlib import Path

claves_none_fix = {
    "sensor_id": "Sensor Desconocido",
    "temperatura": 0,
    "ubicacion": "Ubicacion Desconocida"
}

def procesar_json(ruta: str) -> list[dict]:
    with open(Path(ruta), "r", encoding="utf-8") as f:
        json_dict = json.load(f)
        return json_dict

def limpiar_registro_sensor(registro_raw: list[dict]) -> list[dict]:
    registro_limpio = []
    
    for sensor in registro_raw:
        id_limpia = sensor["sensor_id"].strip() if sensor.get("sensor_id") is not None and sensor.get("sensor_id") != "" else claves_none_fix.get("sensor_id")
        temperatura_limpia = float(sensor.get("temperatura").strip().replace("°C", "").replace("C", "")) if sensor.get("temperatura") and sensor.get("temperatura").strip() else claves_none_fix.get("temperatura")
        ubicacion_limpia = sensor["ubicacion"].strip() if sensor.get("ubicacion") is not None and sensor.get("ubicacion") != "" else claves_none_fix.get("ubicacion")

        registro_limpio.append({
            "sensor_id": id_limpia,
            "temperatura": temperatura_limpia,
            "ubicacion": ubicacion_limpia
        })

    return registro_limpio

def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float) -> tuple[list[str], float]:
    sensores_activos = []
    temperaturas = []

    for sensor in lista_sensores_limpios:
        temperatura = sensor.get("temperatura")

        if temperatura is not None:
            temperaturas.append(temperatura)

            if temperatura > umbral_temperatura:
                sensores_activos.append(sensor.get("sensor_id"))

    promedio = sum(temperaturas) / len(temperaturas) if len(temperaturas) > 0 else 0

    return sensores_activos, float(promedio)

### FLUJO DE EJECUCIÓN

lista_raw = procesar_json("ejercicio_1_sensores/sensores.json")

print("JSON Leído correctamente.")

lista_limpia = limpiar_registro_sensor(lista_raw)

print("Lista limpia.")

umbral = input("Ingrese el umbral de temperatura: ")

try:
    resumen = generar_resumen_sensores(lista_limpia, float(umbral))
except ValueError:
    print("Por favor ingresa un número entero o flotante.")
    resumen = generar_resumen_sensores(lista_limpia, 0)

print("SENSORES ACTIVOS")

for sensor in resumen[0]:
    print(sensor)

print(f"Promedio de temperatura global: {resumen[1]:.2f}")