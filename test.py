import git_exercise
import unittest


class TestCalculation(unittest.TestCase):
    def test_add(self):
        data = (10, 5)
        res = sum(data)
        self.assertEqual(res, 15)

if __name__ == '__main__':
    unittest.main()
    