# parameterized testing

import unittest

from src.tax3 import calc_tax

# class TestCalcTax(unittest.TestCase):
#     def test_calc_tax_twenty_percent_and_eighteen_age(self):
#         self.assertEqual(calc_tax(60000, 0.2, 18), 5000)

#     def test_calc_tax_twenty_percent_and_nineteen_age(self):
#         self.assertEqual(calc_tax(60000, 0.2, 19), 12000)

#     def test_calc_tax_twenty_percent_and_sixty_five_age(self):
#         self.assertEqual(calc_tax(60000, 0.2, 65), 12000)

#     def test_calc_tax_twenty_percent_and_sixty_sik_age(self):
#         self.assertEqual(calc_tax(60000, 0.2, 66), 8000)

# class TestCalcTax(unittest.TestCase):
#     def test_calc_tax(self):
#         test_cases = [
#             (60000, 0.2, 18, 5000),
#             (60000, 0.2, 19, 12000),
#             (60000, 0.2, 65, 12000),
#             (60000, 0.2, 66, 8000),
#         ]

#         for amount, tax_rate, age, expected in test_cases:
#             with self.subTest(
#                 amount = amount,
#                 tax_rate = tax_rate,
#                 age = age,
#                 expected = expected
#         ):
#                 self.assertEqual(calc_tax(amount, tax_rate, age), expected)

from src.rectamgle import area, perimeter

# class TestArea(unittest.TestCase):
    # def test_area(self):
    #     test_cases = [
    #         (1, 5, 5),
    #         (2, 10, 20),
    #         (100, 50, 5000)
    #     ]

    #     for width, height, expected in test_cases:
    #         with self.subTest(
    #             width = width,
    #             height = height,
    #             expected = expected
    #             ):
    #             self.assertEqual(area(width, height), expected)
    
    # def test_area_incorrect_type_should_raise_type_error(self):
    #     test_cases = [
    #         (1, "5", TypeError),
    #         ("2", 10, TypeError),
    #         ("two", "four", TypeError)
    #     ]

    #     for width, height, expected in test_cases:
    #         with self.subTest(
    #             width = width,
    #             height = height, 
    #             expected = expected
    #         ):
    #             self.assertRaises(expected, area, (width, height))
    #             with self.assertRaises(expected):
    #                 area(width, height)

    # def test_area_invalid_value_should_raise_value_error(self):
    #     test_cases = [
    #         (-4, 5, ValueError),
    #         (4, -5, ValueError),
    #         (10, 0, ValueError)
    #     ]

    #     for width, height, expected in test_cases:
    #         with self.subTest(
    #             width = width,
    #             height = height,
    #             expected = expected
    #         ):
    #             self.assertRaises(expected, area, width, height)

# class TestPerimeter(unittest.TestCase):
#     def test_perimeter(self):
#         test_cases = [
#             (1, 5, 12),
#             (2, 10, 24),
#             (100, 50, 300)
#         ]
#         for width, height, expected in test_cases:
#             with self.subTest(
#                 width = width,
#                 height = height,
#                 expected = expected
#             ):
#                 self.assertEqual(perimeter(width, height), expected)
    
#     def test_perimeter_invalid_type_should_raise_type_error(self):
#         test_cases = [
#             (4, "5"),
#             ("2", 8),
#             ("two", "three")
#         ]

#         for width, height in test_cases:
#             with self.subTest(width=width, height=height):
#                 # self.assertRaises(TypeError, perimeter, width, height)
#                 with self.assertRaises(TypeError):
#                     perimeter(width, height)
    
#     def test_perimeter_incorrect_value_should_raise_value_error(self):
#         test_cases = [
#             (-40, 5),
#             (4, -10), 
#             (0, 0)
#         ]

#         for width, height in test_cases:
#             with self.subTest(width = width, height = height):
#                 with self.assertRaises(ValueError):
#                     perimeter(width, height)

# def sum_odd_numbers(numbers):
#     return sum(num for num in numbers if num % 2 == 1)

# class TestSumOddNumbers(unittest.TestCase):
#     def test_sum_odd_numbers(self):
#         test_cases = [
#             ([1, 2, 3, 4, 5], 9), 
#             ([10, 11, 12, 13, 14, 15], 39),
#             ([2, 4, 6], 0),
#             ([], 0),
#             ([1, 3, 5, 7], 16)
#         ]

#         for input, expected in test_cases:
#             with self.subTest(input = input, expected = expected):
#                 self.assertEqual(sum_odd_numbers(input), expected)

# def string_lengths(strings):
#     return list(map(len, strings))

# class TestStringLength(unittest.TestCase):
#     def test_string_length(self):
#         test_cases = [
#             {"input": ['hello', 'world'], "expected": [5, 5]},
#             {"input": ['python', 'is', 'awesome'], "expected":  [6, 2, 7]},
#             {"input": [], "expected":  []},
#             {"input": ['1', '22', '333', '4444'], "expected":  [1, 2, 3, 4]},
#                     ]
#         for test_case in test_cases:
#             with self.subTest(test_case = test_case):
#                 input = test_case['input']
#                 expected = test_case["expected"]
#                 self.assertEqual(string_lengths(input), expected)

# def quotient(numbers):
#     if numbers[1] == 0:
#         raise ValueError('Division by zero')
#     return numbers[0] / numbers[1]

# class TestQuotient(unittest.TestCase):
#     def test_quotient(self):
#         test_cases = [
#             ([1, 2], 0.5),
#             ([10, 5], 2),
#             ([2, 0], None),
#             ([-10, 5], -2),
#             ([0, 1], 0),
#             ([0, 0], None)
#         ]

#         for input, expected in test_cases:
#             with self.subTest(input = input, expected = expected):
#                 if input[1] == 0:
#                     self.assertRaises(ValueError, quotient, input)
#                 else:
#                     self.assertEqual(quotient(input), expected)

# def remove_vowels(input_str):
#     if not isinstance(input_str, str):
#         raise TypeError("Input must be a string")
#     vowels = ["a", "e", "i", "o", "u"]
#     return "".join(
#         [char for char in input_str if char.lower() not in vowels]
#     )

# class TestRemoveVowels(unittest.TestCase):
#     def test_remove_vowels(self):
#         test_cases=[
#             {"input": "hello world", "expected":  "hll wrld"},
#             {"input": "Python is awesome", "expected":  "Pythn s wsm"},
#             {"input": "aeiou", "expected":  ""},
#             {"input": "", "expected":  ""},
#             {"input": ["not a string"], "expected":  None},
#             {"input": {"not a string": "value"}, "expected":  None},
#             {"input": None, "expected":  None}
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case = test_case):
#                 if not isinstance(test_case["input"], str):
#                     self.assertRaises(TypeError, remove_vowels, test_case["input"])
#                 else:
#                     self.assertEqual(remove_vowels(test_case["input"]), test_case["expected"])

# def reverse_dict(input_dict):
#     if not isinstance(input_dict, dict):
#         raise TypeError("Input must be a dictionary")
#     for key, value in input_dict.items():
#         if not isinstance(value, int):
#             raise ValueError("All values must be integers")
#     return {value: key for key, value in input_dict.items()}

# class TestReverseDict(unittest.TestCase):
#     def test_reverse_dict(self):
#         test_cases = [
#             ({"one": 1, "two": 2, "three": 3}, {1: "one", 2: "two", 3: "three"}),
#             ({"a": 0, "b": -1, "c": 10}, {0: "a", -1: "b", 10: "c"}),
#             ([], []),
#             ({"one": "1", "two": 2, "three": 3}, None),
#             (["not a dictionary"], None),
#             ({"one": 1, "two": "2", "three": 3}, None ),
#             ({"one": 1, "two": 2, "three": "3"}, None),
#             ({"one": 1, "two": 2, 3: "three"}, None)
#         ]

#         for input, expected in test_cases:
#             with self.subTest(input = input, expected = expected):
#                 if not isinstance(input, dict):
#                     self.assertRaises(TypeError, reverse_dict, input)
#                 elif not all(
#                     isinstance(value, int)
                    
#                     for value in input.values()):
#                     self.assertRaises(ValueError, reverse_dict, input)
#                 else:
#                     self.assertEqual(reverse_dict(input), expected)

# -----------------------------------------------------------------
# parameterized module

from parameterized import parameterized

# def sum_even_numbers(numbers):
#     return sum(filter(lambda x: x % 2 == 0, numbers))

# class TestSumEvenNumbers(unittest.TestCase):

#     @parameterized.expand([
#         ([1, 2, 3, 4, 5], 6),
#         ([10, 20, 30, 40, 50], 150),
#         ([1, 3, 5, 7, 9], 0),
#         ([0, 2, 4, 6, 8], 20),
#         ([], 0)
#                 ])

#     def test_sum_even_numbers(self, input, expected):
#         result = sum_even_numbers(input)
#         self.assertEqual(result, expected)

# def reverse_string(input_str):
#     return input_str[::-1]

# class TestReverseString(unittest.TestCase):

#     @parameterized.expand([
#         ("hello", "olleh"),
#         ("python", "nohtyp"),
#         ("racecar", "racecar"),
#         ("12345", "54321"),
#         ("", "")
#     ])

#     def test_reverse_string(self, input, expected):
#         self.assertEqual(reverse_string(input), expected)

# def square_pairs(numbers):
#     return [(x, x**2) for x in numbers]

# class TestSquarePairs(unittest.TestCase):

#     @parameterized.expand([
#         ([1, 2, 3, 4, 5], [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]),
#         ([-1, 0, 1], [(-1, 1), (0, 0), (1, 1)]),
#         ([], []),
#         ([2**31-1], [(2**31-1, (2**31-1)**2)])
#     ])

#     def test_square_pairs(self, input, expected):
#         self.assertEqual(square_pairs(input), expected)

# def average(numbers):
#     if not isinstance(numbers, list):
#         raise TypeError("Input must be a list")
#     if len(numbers) == 0:
#         raise ValueError("List must not be empty")
#     return sum(numbers) / len(numbers)
# class TestAverage(unittest.TestCase):

#     @parameterized.expand([
#         ([1, 2, 3], 2),
#         ([10, 20, 30, 40], 25),
#         ([5], 5),
#         ([0, 0, 0], 0),
#         ([], None),
#         (["not a number"], None),
#         (["1", 2, 3], None),
#         ([None],  None)
#     ])

#     def test_average(self, input, expected):
#         if expected is None:
#             with self.assertRaises((TypeError, ValueError)):
#                 average(input)
#         else: 
#             self.assertEqual(average(input), expected)

def sort_strings(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    for item in input_list:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
    return sorted(input_list)

class TestSortStrings(unittest.TestCase):

    @parameterized.expand([
        (["hello", "world"], ["hello", "world"]),
        (["z", "a", "c"], ["a", "c", "z"]),
        ([], []),
        (["hello", 123], None),
        ({"not": "a list"}, None),
        (["hello", None], None)
    ])

    def test_sort_strings(self, input, expected):
        if expected is None:
            self.assertRaises((TypeError, ValueError))
        else:
            self.assertEqual(sort_strings(input), expected)

'''
For each test case, we use an if statement to check if the expected output is None. If it is, we use the assertRaises method with a tuple of exceptions to check that the function raises either a TypeError or ValueError. If it is not None, we use the assertEqual method to check that the function returns the correct sorted list.
'''

if __name__== "__main__":
    unittest.main()