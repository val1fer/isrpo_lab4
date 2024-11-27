import unittest

class SquareTestCase(unittest.TestCase):

    def test_square_area_1(self):
        res = area(20)
        self.assertEqual(res, 400)
        
    def test_square_area_2(self):
        res = area(50)
        self.assertEqual(res, 2500)

    def test_square_perimeter_1(self):
        res = perimeter(5*27)
        self.assertEqual(res,(5*27) * 4)
    
    def test_square_perimeter_2(self):
        res = perimeter(18)
        self.assertEqual(res, 18 * 4)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)




def area(a):
    return a * a
    
def perimeter(a):
    return 4 * a
  
