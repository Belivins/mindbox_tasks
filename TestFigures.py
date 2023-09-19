import unittest
from Figures import Triangle, Circle


class TestTriangle(unittest.TestCase):

    def test_triangle_exist(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 1, 1)
        with self.assertRaises(ValueError):
            Triangle(1, 0, 1)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)
        with self.assertRaises(ValueError):
            Triangle(5, 1, 1)
        with self.assertRaises(ValueError):
            Triangle(1, 3, 2)
        with self.assertRaises(ValueError):
            Triangle(101, 1.1, 11)
        self.assertEqual(Triangle(5, 3, 4).exist(), True)
        self.assertEqual(Triangle(1, 1, 1).exist(), True)
        self.assertEqual(Triangle(1.1, 1.1, 1.1).exist(), True)
        self.assertEqual(Triangle(4, 2, 3).exist(), True)

    def test_triangle_perimetr(self):
        self.assertEqual(Triangle(5, 3, 4).perimeter(), 12)
        self.assertEqual(Triangle(1, 1, 1).perimeter(), 3)
        self.assertAlmostEqual(Triangle(1.1, 1.1, 1.1).perimeter(), 3.300, places=3)
        # self.assertEqual(Triangle(1.1, 1.1, 1.1).perimeter(), 3.3)
        self.assertEqual(Triangle(4, 2, 3).perimeter(), 9)

    def test_triangle_area(self):
        self.assertEqual(Triangle(5, 3, 4).area(), 6)
        self.assertAlmostEqual(Triangle(1, 1, 1).area(), 0.433, places=3)
        self.assertAlmostEqual(Triangle(1.1, 1.1, 1.1).area(), 0.524, places=3)
        self.assertAlmostEqual(Triangle(4, 2, 3).area(), 2.905, places=3)

    def test_triangle_rectangular(self):
        self.assertEqual(Triangle(5, 3, 4).is_rectangular(), True)
        self.assertEqual(Triangle(1, 1, 1).is_rectangular(), False)
        self.assertEqual(Triangle(1.1, 1.1, 1.1).is_rectangular(), False)
        self.assertEqual(Triangle(4, 2, 3).is_rectangular(), False)


class TestCircle(unittest.TestCase):

    def test_circle_exist(self):
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-0.1)

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(1).area(), 3.142, places=3)
        self.assertAlmostEqual(Circle(3).area(), 28.274, places=3)
        self.assertAlmostEqual(Circle(0.1).area(), 0.031, places=3)


if __name__ == "__main__":
    unittest.main()
