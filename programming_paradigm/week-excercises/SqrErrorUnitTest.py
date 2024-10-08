import unittest

class TestCalculateSquare(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(TestCalculateSquare(5), 25)  # This will fail due to the bug
        self.assertEqual(TestCalculateSquare(0), 0)   # This will pass
        self.assertEqual(TestCalculateSquare(-3), 9)  # This will fail due to the bug

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            TestCalculateSquare("a")  # This should raise a TypeError

if __name__ == '__main__':
    unittest.main()
