import compare
import unittest


class TestGeneration(unittest.TestCase):

    def test_check_values(self):
        test_cases = [([1, 2, 3], [1, 2, 3], False),
                      ([1, 3, 3], [1, 2, 3], True)]
        for test in test_cases:
            check, _ = compare.check_values(test[0], test[1])
            self.assertEqual(check, test[2], "Expected %s" % str(test[2]))


if __name__ == '__main__':
    unittest.main()
