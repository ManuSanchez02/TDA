import random
import unittest

from dinamica import sobornar_dinamico
from greedy import sobornar_greedy
from utils import generar_contrabando

random.seed(10)


class TestSoborno(unittest.TestCase):

    def assertCorrectPackages(self, solution, expected):
        for product, packages in solution.items():
            solution[product] = sum(packages)

        self.assertEqual(solution, expected)

    def assertCorrectPackagesOrMore(self, solution, expected):
        for product, packages in solution.items():
            self.assertGreaterEqual(sum(packages), expected[product])

    def setUp(self):
        self.soborno_dinamico = sobornar_dinamico
        self.soborno_greedy = sobornar_greedy

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
            'Cigarrillo': 8
        }

        self.assertCorrectPackages(
            self.soborno_dinamico(self.mercaderia_ejemplo, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(self.mercaderia_ejemplo, soborno), solucion)

    def test_ejemplo_2_consigna(self):
        soborno = {
            "Cigarrillo": 10
        }

        solucion = {
            'Cigarrillo': 13
        }

        self.assertCorrectPackages(
            self.soborno_dinamico(self.mercaderia_ejemplo, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(self.mercaderia_ejemplo, soborno), solucion)

    def test_ejemplo_3_consigna(self):
        soborno = {
            "Cigarrillo": 1,
            "Vodka": 1
        }
        solucion = {
            'Cigarrillo': 5,
            'Vodka': 5
        }

        self.assertCorrectPackages(
            self.soborno_dinamico(self.mercaderia_ejemplo, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(self.mercaderia_ejemplo, soborno), solucion)

    def test_solucion_sin_paquete_grande(self):
        mercaderia = {
            "Cigarrillo": [8, 6, 5]
        }

        soborno = {
            "Cigarrillo": 11
        }

        solucion = {
            "Cigarrillo": 11
        }

        self.assertCorrectPackages(
            self.soborno_dinamico(mercaderia, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(mercaderia, soborno), solucion)

    def test_soborno_0(self):
        soborno = {
            "Cigarrillo": 0,
            "Vodka": 0
        }

        solucion = {
            "Cigarrillo": 0,
            "Vodka": 0
        }

        self.assertCorrectPackages(
            self.soborno_dinamico(self.mercaderia_ejemplo, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(self.mercaderia_ejemplo, soborno), solucion)

    def test_volume(self):
        k = 50
        n = 100

        mercaderia, solucion, soborno = generar_contrabando(n, k)

        self.assertCorrectPackages(
            self.soborno_dinamico(mercaderia, soborno), solucion)

        self.assertCorrectPackagesOrMore(
            self.soborno_greedy(mercaderia, soborno), solucion)


if __name__ == '__main__':
    unittest.main()
