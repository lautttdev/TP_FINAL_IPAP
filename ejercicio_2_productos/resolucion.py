import json
from pathlib import Path

# Excepcion Personalizada

class StockInvalidoError(Exception):
    pass

# Productos

class DispositivoEcologico:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def agregar_stock(self, unidades):
        self._stock += unidades

        print(f"{unidades} de {self.nombre} agregadas correctamente.")

    def quitar_stock(self, unidades):
        try:
            if self.stock - unidades < 0:
                raise StockInvalidoError(f"No hay tal cantidad de unidades en Stock de {self.nombre}. {self.stock} unidades restantes.")
            
            self._stock -= unidades

            print(f"{unidades} de {self.nombre} quitadas correctamente.")
            
        except StockInvalidoError as e:
            print(f"Error de inventario: {e}")

    def to_dict(self):
        return {
            "tipo": "DispositivoEcologico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    def __repr__(self):
        return f"{self._nombre}, ${self._precio}, {self._stock} unidad/es"

    def __str__(self):
        return f"{self._nombre}, ${self._precio}, {self._stock} unidad/es"

class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, precio, stock, potencia_w):
        super().__init__(nombre, precio, stock)

        self._potencia_w = potencia_w

    @property
    def potencia_w(self):
        return self._potencia_w

    def to_dict(self):
        return {
            "tipo": "Panel Solar",
            "nombre": self.nombre,
            "potencia": self.potencia_w,
            "precio": self.precio,
            "stock": self.stock
        }

    def __repr__(self):
        return f"{self._nombre}, {self._potencia_w}w, ${self._precio}, {self._stock} unidad/es"

    def __str__(self):
        return f"{self._nombre}, {self._potencia_w}w, ${self._precio}, {self._stock} unidad/es"

# Gestor de Inventario

class GestorInventario:
    def __init__(self):
        pass

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.to_dict())

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(catalogo, f, indent=4, ensure_ascii=False)

# Flujo de ejecución

gestor_inv = GestorInventario()

print("Gestor inicializado correctamente.")

panel_solar_600 = PanelSolar("Panel Solar 600W", 15000, 10, 600)
panel_solar_500 = PanelSolar("Panel Solar 500W", 13000, 5, 500)

print("Productos inicializados correctamente.")

# Captura de error
panel_solar_600.quitar_stock(11)

panel_solar_500.agregar_stock(20)
panel_solar_500.quitar_stock(15)

gestor_inv.guardar_catalogo_json([panel_solar_500, panel_solar_600], "ejercicio_2_productos/catalogo_ecotech.json")

print("Catalogo guardado correctamente.")