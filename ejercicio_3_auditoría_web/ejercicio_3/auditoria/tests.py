import unittest
from .utils import calcular_emisiones_carbono

# Create your tests here.

#uv run python manage.py test auditoria

class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo(self):
        self.assertEqual(calcular_emisiones_carbono(100), 40, "El resultado es el esperado.")

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)

    def test_factor_emision_variable(self):
        self.assertEqual(calcular_emisiones_carbono(20, 0.6), 12, "El resultado es el esperado.")
