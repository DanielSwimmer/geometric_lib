import unittest
from circle import area as S 
from circle import perimeter as P

class CirlceTestCase(unittest.TestCase):
   def test_zero_radius(self):
       res = S(0)
       self.assertEqual(res, 0)
       res = P(0)
       self.assertEqual(res, 0)

   def test_negativ_valueS(self):
       with self.assertRaises(ValueError):
           S(-1)

   def test_negativ_valueP(self):
       with self.assertRaises(ValueError):
           P(-1)

   def test_type_valueS(self):
       with self.assertRaises(TypeError):
           S("1")

   def test_type_valueP(self):
       with self.assertRaises(TypeError):
           P("1")

   def test_standart_area(self):
       res = S(10)
       self.assertEqual(res, 314.1592653589793)

   def test_standart_perimetr(self):
       res = P(10)
       self.assertEqual(res, 62.83185307179586)