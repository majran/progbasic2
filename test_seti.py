import unittest
import seti.seti_converter as seti

binary_decimal = (
    {"decimal": 100, "binary": [1, 1, 0, 0, 1, 0, 0]},
    {"decimal": 2, "binary": [1, 0]},
    {"decimal": 0, "binary": [0]},
    {"decimal": 1, "binary": [1]},
    {"decimal": 64, "binary": [1, 0, 0, 0, 0, 0, 0]},
)

decimal_base = (
    {"decimal": 100, "base": 2, "result": [1, 1, 0, 0, 1, 0, 0]},
    {"decimal": 2, "base": 2, "result": [1, 0]},
    {"decimal": 0, "base": 2, "result": [0]},
    {"decimal": 1, "base": 2, "result": [1]},
    {"decimal": 64, "base": 2, "result": [1, 0, 0, 0, 0, 0, 0]},

    {"decimal": 100, "base": 8, "result": [1, 4, 4]},
    {"decimal": 8, "base": 8, "result": [1, 0]},
    {"decimal": 0, "base": 8, "result": [0]},
    {"decimal": 1, "base": 8, "result": [1]},
    {"decimal": 64, "base": 8, "result": [1, 0, 0]},

    {"decimal": 1000, "base": 16, "result": [3, 14, 8]},
    {"decimal": 16, "base": 16, "result": [1, 0]},
    {"decimal": 0, "base": 16, "result": [0]},
    {"decimal": 1, "base": 16, "result": [1]},
    {"decimal": 6598165148651321, "base": 16, "result": [1, 7, 7, 0, 15, 15, 0, 9, 13, 10, 12, 15, 3, 9]}
)

any_to_any_base = (
    {"digits": [1, 0, 0], "source": 10, "target": 2, "result": [1, 1, 0, 0, 1, 0, 0]},
    {"digits": [5, 1, 5], "source": 8, "target": 16, "result": [1, 4, 13]},
    {"digits": [1, 4, 13], "source": 16, "target": 8, "result": [5, 1, 5]},
)

digit_as_string = (
    {"digits": [0], "base": 2, "expected": "0"},
    {"digits": [1], "base": 2, "expected": "1"},
    {"digits": [1, 0], "base": 2, "expected": "10"},
    {"digits": [10], "base": 16, "expected": "A"},
    {"digits": [1, 0], "base": 8, "expected": "10"},
    {"digits": [10, 11, 12, 13, 14, 15], "base": 16, "expected": "ABCDEF"},
    {"digits": [1, 2, 0, 10], "base": 16, "expected": "120A"},
    {"digits": [1, 7, 7, 0, 15, 15, 0, 9, 13, 10, 12, 15, 3, 9], "base": 16, "expected": "1770FF09DACF39"},
)

digit_as_string_exception = (
    {"digits": [], "base": 2, "expected": ""},
    {"digits": [1], "base": 0, "expected": ""},
    {"digits": [1], "base": 17, "expected": ""},
    {"digits": [17, 0, 1], "base": 16, "expected": ""},
)


class TestSum(unittest.TestCase):

    def test_decimal_to_binary(self):
        for test_case in binary_decimal:
            with self.subTest(f"b:{test_case['decimal']} = d: {list(test_case['binary'])}"):
                self.assertEqual(
                    seti.decimal_to_binary(test_case['decimal']),
                    test_case['binary'])

    def test_binary_to_decimal(self):
        for test_case in binary_decimal:
            with self.subTest(f"b:{test_case['binary']} = d: {test_case['decimal']}"):
                self.assertEqual(
                    seti.binary_to_decimal(test_case['binary']),
                    test_case['decimal'])

    def test_decimal_to_any_base(self):
        for test_case in decimal_base:
            with self.subTest(f"d:{test_case['decimal']} = {test_case['base']}x: {test_case['result']}"):
                self.assertEqual(
                    seti.decimal_to_base(test_case['decimal'], test_case['base']),
                    test_case['result'])

    def test_any_base_to_decimal(self):
        for test_case in decimal_base:
            test_case_name = f"{test_case['base']}x: {test_case['result']} =  d: {test_case['decimal']}"
            with self.subTest(test_case):
                actual = seti.base_to_decimal(test_case['result'], test_case['base'])
                expected = test_case['decimal']
                print(test_case_name + f" => actual result {actual}")
                self.assertEqual(actual, expected)

    def test_string_representation(self):
        for test_case in digit_as_string:
            with self.subTest(f"{test_case['digits']} = {test_case['base']}x: {test_case['expected']}"):
                self.assertEqual(
                    seti.digits_as_string(test_case['digits'], test_case['base']),
                    test_case['expected'])

    def test_string_representation_exception(self):
        for test_case in digit_as_string_exception:
            with self.subTest(f"{test_case['digits']} = {test_case['base']}x: {test_case['expected']}"):
                with self.assertRaises(ValueError):
                    seti.digits_as_string(test_case['digits'], test_case['base'])

    def test_any_to_any_base(self):
        for test_case in any_to_any_base:
            with self.subTest(test_case):
                self.assertEqual(
                    seti.convert_base(test_case['digits'], test_case['source'], test_case['target']),
                    test_case['result'])


if __name__ == '__main__':
    unittest.main()
