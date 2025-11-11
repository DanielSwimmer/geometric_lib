import unittest
from rectangle import area as S 
from rectangle import perimeter as P

class RectangleTestCase(unittest.TestCase):
   def test_zero_side(self):
       res = S(0, 10)
       self.assertEqual(res, 0)
       res = P(0, 0)
       self.assertEqual(res, 0)

   def test_negativ_valueS(self):
       with self.assertRaises(ValueError):
           S(-1, 1)
       with self.assertRaises(ValueError):
           S(1, -1)

   def test_negativ_valueP(self):
       with self.assertRaises(ValueError):
           P(-1, 1)
       with self.assertRaises(ValueError):
           P(1, -1)

   def test_type_valueS(self):
       with self.assertRaises(TypeError):
           S("1",1 )
       with self.assertRaises(TypeError):
           S(1, "1") 

   def test_type_valueP(self):
       with self.assertRaises(TypeError):
           P("1", 1)
       with self.assertRaises(TypeError):
           P(1, "1")  

   def test_standart_area(self):
       res = S(10, 10)
       self.assertEqual(res, 100)

   def test_standart_perimetr(self):
       res = P(10, 10)
       self.assertEqual(res, 40)