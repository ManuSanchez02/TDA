import random
import unittest

# from p_dinamica import sobornar
from dinamica import sobornar_dinamico
from utils import random_array

random.seed(10)


class TestSoborno(unittest.TestCase):

    def assertCorrectPackages(self, solution, expected):
        for product, packages in solution.items():
            solution[product] = sum(packages)
            expected[product] = sum(expected[product])

        self.assertEqual(solution, expected)

    def setUp(self):
        self.alg_soborno = sobornar_dinamico

        self.mercaderia_ejemplo = {
            'Cigarrillo': [8, 5],
            'Vodka': [5]
        }

        return super().setUp()

    def test_ejemplo_1_consigna(self):
        soborno = {
            "Cigarrillo": 6
        }

        solucion = {
            'Cigarrillo': [8]
        }

        self.assertCorrectPackages(
            self.alg_soborno(self.mercaderia_ejemplo, soborno), solucion)

    def test_ejemplo_2_consigna(self):
        soborno = {
            "Cigarrillo": 10
        }

        solucion = {
            'Cigarrillo': [5, 8]
        }

        self.assertCorrectPackages(
            self.alg_soborno(self.mercaderia_ejemplo, soborno), solucion)

    def test_ejemplo_3_consigna(self):
        soborno = {
            "Cigarrillo": 1,
            "Vodka": 1
        }
        solucion = {
            'Cigarrillo': [5],
            'Vodka': [5]
        }

        self.assertCorrectPackages(
            self.alg_soborno(self.mercaderia_ejemplo, soborno), solucion)

    def test_solucion_sin_paquete_grande(self):
        mercaderia = {
            "Cigarrillo": [8, 6, 5]
        }

        soborno = {
            "Cigarrillo": 11
        }

        solucion = {
            "Cigarrillo": [6, 5]
        }

        self.assertCorrectPackages(self.alg_soborno(mercaderia, soborno), solucion)

    def test_soborno_0(self):
        soborno = {
            "Cigarrillo": 0,
            "Vodka": 0
        }

        solucion = {
            "Cigarrillo": [],
            "Vodka": []
        }

        self.assertCorrectPackages(
            self.alg_soborno(self.mercaderia_ejemplo, soborno), solucion)

    def test_volume(self):
        self.mercaderia = {}
        self.soborno = {}
        self.optimo = {}

        k = 50
        n = 100

        for i in range(k):
            producto = f"producto{i}"
            paquetes = random_array(n)
            self.mercaderia[producto] = paquetes

            soborno_elegido = random.sample(paquetes, k=n // 3)
            self.soborno[producto] = sum(soborno_elegido)
            self.optimo[producto] = soborno_elegido

        self.assertCorrectPackages(self.alg_soborno(self.mercaderia, self.soborno), self.optimo)


if __name__ == '__main__':
    unittest.main()
