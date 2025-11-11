import unittest
import math
import sys
import os

# Добавляем src в путь для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import geometry

class TestRectangleFunctions(unittest.TestCase):
    """Тесты для функций прямоугольника"""
    
    def test_rectangle_area_positive(self):
        """Тест площади прямоугольника с положительными числами"""
        self.assertEqual(geometry.rectangle_area(5, 10), 50)
        self.assertEqual(geometry.rectangle_area(3, 7), 21)
        self.assertEqual(geometry.rectangle_area(2.5, 4), 10.0)
    
    def test_rectangle_area_zero(self):
        """Тест площади прямоугольника с нулевыми сторонами"""
        self.assertEqual(geometry.rectangle_area(0, 10), 0)
        self.assertEqual(geometry.rectangle_area(5, 0), 0)
        self.assertEqual(geometry.rectangle_area(0, 0), 0)
    
    def test_rectangle_area_negative(self):
        """Тест площади прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            geometry.rectangle_area(-5, 10)
    
    def test_rectangle_perimeter_positive(self):
        """Тест периметра прямоугольника с положительными числами"""
        self.assertEqual(geometry.rectangle_perimeter(5, 10), 30)
        self.assertEqual(geometry.rectangle_perimeter(3, 7), 20)

class TestTriangleFunctions(unittest.TestCase):
    """Тесты для функций треугольника"""
    
    def test_triangle_area_heron(self):
        """Тест площади треугольника по формуле Герона"""
        self.assertAlmostEqual(geometry.triangle_area(3, 4, 5), 6.0)
    
    def test_triangle_area_equilateral(self):
        """Тест площади равностороннего треугольника"""
        expected = (25 * math.sqrt(3)) / 4
        self.assertAlmostEqual(geometry.triangle_area(5, 5, 5), expected, places=6)
    
    def test_triangle_area_invalid(self):
        """Тест площади несуществующего треугольника"""
        with self.assertRaises(ValueError):
            geometry.triangle_area(1, 1, 3)

class TestCircleFunctions(unittest.TestCase):
    """Тесты для функций круга"""
    
    def test_circle_area(self):
        """Тест площади круга"""
        self.assertAlmostEqual(geometry.circle_area(1), math.pi)
        self.assertAlmostEqual(geometry.circle_area(2), 4 * math.pi)
    
    def test_circle_perimeter(self):
        """Тест периметра круга"""
        self.assertAlmostEqual(geometry.circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(geometry.circle_perimeter(2), 4 * math.pi)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main(verbosity=2)