import unittest
from main import app
from mymath import quadratic_equation



class FrameworkTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200) #успех http


    def test_quadratic_equation_one_root(self):
        response = quadratic_equation(10, 0, 0)
        self.assertEqual(response, "Корни уравнения равны: 0j и 0j")

    def test_quadratic_equation_multy_root(self):
        response = quadratic_equation(2, 5, -3)
        self.assertEqual(response, "Корни уравнения равны: (-3+0j) и (0.5+0j)")

    




