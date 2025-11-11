import unittest
from triangle import area as S 
from triangle import perimeter as P

class TriangleTestCase(unittest.TestCase):
   def test_zero_side(self):
       res = S(0, 0)
       self.assertEqual(res, 0)

   def test_negativ_valueS(self):
       with self.assertRaises(ValueError):
           S(-1, 1)
       with self.assertRaises(ValueError):
           S(1, -1)

   def test_negativ_valueP(self):
       with self.assertRaises(ValueError):
           P(-1, 1, 1)
       with self.assertRaises(ValueError):
           P(1, -1, 1)
       with self.assertRaises(ValueError):
           P(1, 1, -1)

   def test_type_valueS(self):
       with self.assertRaises(TypeError):
           S("1",1 )
       with self.assertRaises(TypeError):
           S(1, "1") 

   def test_type_valueP(self):
       with self.assertRaises(TypeError):
           P("1", 1, 1)
       with self.assertRaises(TypeError):
           P(1, "1", 1)
       with self.assertRaises(TypeError):
           P(1, 1, "1")

   def test_real_triangle(self):
       with self.assertRaises(ValueError):
           P(10, 1, 1)
       with self.assertRaises(ValueError):
           P(1, 10, 1)
       with self.assertRaises(ValueError):
           P(1, 1, 10)

   def test_standart_area(self):
       res = S(10, 10)
       self.assertEqual(res, 50)

   def test_standart_perimetr(self):
       res = P(10, 10, 10)
       self.assertEqual(res, 30)