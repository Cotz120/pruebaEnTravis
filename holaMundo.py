import unittest
from sumas import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        numeros = [3, 5, 4]
        resultado = sum(numeros)
        self.assertEqual(resultado, 10)

if __name__ == '__main__':
    unittest.main()