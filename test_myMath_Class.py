import unittest
#from unittest import TestCase

from MyMath import MyMath_Class

class TestMyMath_Class(unittest.TestCase):
    def test_calculate_discriminant(self):
        Discriminant = MyMath_Class.calculate_discriminant(4, 10, 4)
        self.assertEqual(Discriminant, 36)

        Discriminant = MyMath_Class.calculate_discriminant(2, 4, 2)
        self.assertEqual(Discriminant, 0)

        Discriminant = MyMath_Class.calculate_discriminant(2, 2, 2)
        self.assertEqual(Discriminant, -12)

    def test_calculate_discriminant_self(self):
        Math_Obj = MyMath_Class()

        Discriminant = Math_Obj.calculate_discriminant_self(4, 10, 4)
        self.assertEqual(Discriminant, 36)

        Discriminant = Math_Obj.calculate_discriminant_self(2, 4, 2)
        self.assertEqual(Discriminant, 0)

        Discriminant = Math_Obj.calculate_discriminant_self(2, 2, 2)
        self.assertEqual(Discriminant, -12)



if __name__ == '__main__':
    unittest.main()