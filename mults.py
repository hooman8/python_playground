import unittest


def multiply(x, y):
    return x + y


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        test_x = 5
        text_y = 10
        self.assertEqual(multiply(test_x, text_y), 50)


# if __name__ == "__main__":
#     unittest.main()

# or

# python -m unittest multy -v
