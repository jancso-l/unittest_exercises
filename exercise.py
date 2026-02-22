# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     """
#     return width * height

# assert rectangle_area(4,10) == 40
# assert rectangle_area(5, 6) == 30

# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     :raises TypeError: If the width or height is not an integer.
#     :raises ValueError: If the width or height is not a positive integer.
#     """
#     if not isinstance(width, int) or not isinstance(height, int):
#         raise TypeError('The width and height must be integers.')
#     if width <= 0 or height <= 0:
#         raise ValueError(
#             'The width and height must be positive integers.'
#         )
#     return width * height


# # Enter your solution here

# assert rectangle_area(-4, 5) == 20

# def calculate_income_tax(
#     amount: float, tax_rate: float, age: int
# ) -> int:
#     """
#     Calculates the income tax based on the given amount, tax rate, 
#     and age.
 
#     :param amount: The amount of income.
#     :param tax_rate: The tax rate as a decimal.
#     :param age: The age of the taxpayer.
#     :return: The amount of income tax.
#     """
#     if age <= 18:
#         return int(min(amount * tax_rate, 5000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 8000))


# # Enter your solution here
# def test_calculate_income_tax():
#     assert calculate_income_tax(60000, 0.15, 10) == 5000        
#     assert calculate_income_tax(60000, 0.15, 18) == 5000
#     assert calculate_income_tax(60000, 0.15, 19) == 9000
#     assert calculate_income_tax(60000, 0.15, 65) == 9000
#     assert calculate_income_tax(60000, 0.15, 66) == 8000

# if __name__ == "__main__":
#     test_calculate_income_tax()

# def factorial(n: int) -> int:
#     """
#     Calculates the factorial of a positive integer.

#     :param n: The integer to calculate the factorial of.
#     :return: The factorial of the integer.
#     :raises ValueError: If the integer is negative.
#     """
#     if n < 0:
#         raise ValueError(
#             'Cannot calculate factorial of a negative number.'
#         )
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
        
# # Enter your solution here 

# assert factorial(0) == 1
# assert factorial(1) == 1
# assert factorial(5) == 120

# try:
#     factorial(-1)
#     assert False
# except ValueError:
#     pass

# def is_palindrome(string: str) -> bool:
#     """
#     Determines whether the given string is a palindrome.

#     :param string: The string to check.
#     :return: True if the string is a palindrome, False otherwise.
#     """
#     string = string.lower().replace(" ", "")
#     return string == string[::-1]
    
# # Enter your solution here
# def test_is_palindrome():
#     assert is_palindrome("racecar") == True
#     assert is_palindrome("hello") == False
#     assert is_palindrome("A man a plan a canal Panama") == True
#     assert is_palindrome("12321") == True
#     assert is_palindrome("not a palindrome") == False

# if __name__ == '__main__':
#     test_is_palindrome()

# def find_max_min(numbers: list) -> tuple:
#     """
#     Finds the maximum and minimum values in the given list.

#     :param numbers: The list of numbers.
#     :return: A tuple containing the maximum and minimum values.
#     :raises ValueError: If the list is empty.
#     """
#     if not numbers:
#         raise ValueError("List is empty")

#     maximum = minimum = numbers[0]

#     for number in numbers[1:]:
#         if number > maximum:
#             maximum = number
#         elif number < minimum:
#             minimum = number

#     return maximum, minimum
    
    
# # Enter your solution here
# def test_find_max_min():
#     assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
#     assert find_max_min([10, 5, 7, 3, 8]) == (10, 3)
#     assert find_max_min([-1, -2, -3, -4, -5]) == (-1, -5)
#     assert find_max_min([0]) == (0, 0)

#     try:
#         find_max_min([])
#         assert False
#     except ValueError:
#         pass

# if __name__ == '__main__':
#     test_find_max_min()

# def gcd(a: int, b: int) -> int:
#     """
#     Calculates the greatest common divisor of two integers.

#     :param a: The first integer.
#     :param b: The second integer.
#     :return: The greatest common divisor of the two integers.
#     """
#     while b:
#         a, b = b, a % b
#     return a


# # Enter your solution here

# assert gcd(8, 12) == 4
# assert gcd(17,23) == 1
# assert gcd(40, 60) == 20
# assert gcd(0, 5) == 5

# def calculate_median(numbers: list) -> float:
#     """
#     Calculates the median value of the given list of numbers.

#     :param numbers: The list of numbers.
#     :return: The median value.
#     :raises ValueError: If the list is empty.
#     """
#     if not numbers:
#         raise ValueError("List is empty")
#     sorted_nums = sorted(numbers)
#     length = len(sorted_nums)

#     if length % 2 == 0:
#         return (
#             sorted_nums[length // 2 - 1] + sorted_nums[length // 2]
#         ) / 2
#     else:
#         return sorted_nums[length // 2]


# # Enter your solution here
# def test_calculate_median():
#     assert calculate_median([1, 2, 3]) == 2
#     assert calculate_median([4, 5, 6, 7]) == 5.5
#     assert calculate_median([2, 1, 3]) == 2
#     assert calculate_median([0, 0, 0, 0]) == 0

#     try:
#         calculate_median([])
#         assert False
#     except ValueError:
#         pass

# if __name__ == '__main__':
#     test_calculate_median()
import unittest

# class TestSplitMethod(unittest.TestCase):
#     '''
#     Tests various split methods.
#     : return: Tests
#     '''

#     def test_split_by_default(self):
#         result = 'Python Testing'.split()
#         self.assertEqual(result, ['Python', 'Testing'])
    
#     def test_split_by_comma(self):
#         result = 'open,high,low,close'.split(',')
#         self.assertEqual(result,  ['open', 'high', 'low', 'close'])

#     def test_split_by_hash(self):
#         result = 'summer#time#vibes'.split('#')
#         self.assertEqual(result, ['summer', 'time', 'vibes']) 

# class TestJoinMethod(unittest.TestCase):
    
#     def test_join_with_space(self):
#         actual = ' '.join(['Python', '3.8'])
#         expected = 'Python 3.8'
#         self.assertEqual(actual, expected)
    
#     def test_join_with_comma(self):
#         actual = ','.join(['open', 'high', 'low', 'close'])
#         expected = 'open,high,low,close'
#         self.assertEqual(actual, expected)
    
#     def test_join_with_new_line_char(self):
#         actual = '\n'.join(['open', 'high', 'low', 'close'])
#         expected = 'open\nhigh\nlow\nclose'
#         self.assertEqual(actual, expected)

# class TestUpper(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('summer'.upper(), 'SUMMER')
    
#     def test_is_upper(self):
#         self.assertTrue('SUMMMER'.isupper())
#         self.assertFalse('summer'.isupper())

# class TestStartsWithMethod(unittest.TestCase):
#     def test_startswith_one_letter(self):
#         self.assertTrue('unittest'.startswith('u'))
#         self.assertFalse('unittest'.startswith('U'))

#     def test_startswith_four_letters(self):
#         self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
#         self.assertFalse('www.e-smartdata.org/'.startswith('http'))

# class TestEndsWithMethod(unittest.TestCase):
#     def test_endswith_three_letter(self):
#         self.assertTrue('e-smartdata.org'.endswith('org')) 
#         self.assertFalse('e-smartdata.org'.endswith('com'))

# class TestLstripMethod(unittest.TestCase):
#     def test_lstrip_with_whitespace(self):
#         self.assertEqual('   spacious   '.lstrip(), 'spacious   ')
    
#     def test_lstrip_with_character(self):
#         self.assertEqual('www.example.com'.lstrip('cmowz.'), 'example.com')

# class TestStripMethod(unittest.TestCase):
#     def test_strip_with_whitespace(self):
#         self.assertEqual('   spacious   '.strip(), 'spacious')
    
#     def test_strip_with_character(self):
#         self.assertEqual('www.example.com'.strip('cmowz.'), 'example')

# class TestRstripMethod(unittest.TestCase):
#     def test_rstrip_with_whitespace(self):
#         self.assertEqual('   spacious   '.rstrip(), '   spacious')
    
#     def test_rstrip_with_character(self):
#         self.assertEqual('mississippi'.rstrip('ipz'), 'mississ')

# class StringReverser:
#     def reverse(self, string):
#         return string[::-1]
    
# class TestStringReverser(unittest.TestCase):
#     def test_reverse(self):
#         reverser = StringReverser()

#         result1 = StringReverser.reverse(self, 'hello')
#         result2 = StringReverser.reverse(self, '12345')
#         result3 = StringReverser.reverse(self, '')
#         self.assertEqual(result1, "olleh")
#         self.assertEqual(result2, "54321")
#         self.assertEqual(result3, "")

# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self._validate_params(width, height)
#         self.width = width
#         self.height = height

#     def _validate_params(self, width: float, height: float) -> None:
#         if not isinstance(width, (int, float)) or width < 0:
#             raise ValueError("Width must be a positive number")
#         if not isinstance(height, (int, float)) or height < 0:
#             raise ValueError("Height must be a positive number")

#     def area(self) -> float:
#         return self.width * self.height
    
# class TestRectangle(unittest.TestCase):
#     def test_area_with_nonzero_dimensions(self):
#         rectangle = Rectangle(3,2)
#         self.assertEqual(rectangle.area(), 6)
#     def test_area_with_zero_dimensions(self):
#         rectangle = Rectangle(0,0)
#         self.assertEqual(rectangle.area(), 0)

#     def test_area_with_negative_width(self):
#         with self.assertRaises(ValueError):
#             rectangle = Rectangle(-3,2)

#     def test_area_with_negative_height(self):
#         with self.assertRaises(ValueError):
#             rectangle = Rectangle(3, -2)

#     def test_area_with_float_dimensions(self):
#         rectangle = Rectangle(3.5,2.7)
#         self.assertAlmostEqual(rectangle.area(), 9.45)

#     def test_area_with_large_dimensions(self):
#         rectangle = Rectangle(20000, 30000)
#         self.assertEqual(rectangle.area(), 600000000)

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius: float) -> float:
#         return (celsius * 9 / 5) + 32

# class TestTemperatureConverter(unittest.TestCase):
#     converter = TemperatureConverter()
#     def test_celsius_to_fahrenheit(self):
#         result1 = self.converter.celsius_to_fahrenheit(0)
#         result2 = self.converter.celsius_to_fahrenheit(100)
#         result3 = self.converter.celsius_to_fahrenheit(-40)
#         self.assertAlmostEqual(result1, 32)
#         self.assertAlmostEqual(result2, 212)
#         self.assertAlmostEqual(result3, -40)

# def calculate_average(numbers):
#     if not numbers:
#         return None
#     return sum(numbers) / len(numbers)

# class TestCalculateAverage(unittest.TestCase):
#     def test_calculate_average_valid_input(self):
#         result1 = calculate_average([1,2,3])
#         self.assertEqual(result1, 2)
#         result2 = calculate_average([0,0,0,0])
#         self.assertEqual(result2, 0)
#         result3 = calculate_average([-1, -2, -3])
#         self.assertEqual(result3, -2)
    
#     def test_calculate_average_empty_input(self):
#         result = calculate_average([])
#         self.assertIsNone(result)
    
#     def test_calculate_average_invalid_input(self):
#         self.assertRaises(TypeError, calculate_average, ['a', 'b', 'c'])
#         with self.assertRaises(TypeError):
#             calculate_average([1, 2, "3", 5])
#         self.assertRaises(TypeError, calculate_average, [None, None])

def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

class TestFindLargest(unittest.TestCase):
    def test_find_largest_valid_input(self):
        result1 = find_largest([1,2,3])
        self.assertEqual(result1, 3)
        
        result2 = find_largest([-1,-2,-3])
        self.assertEqual(result2, -1)

        result3 = find_largest([0, 0, 0])
        self.assertEqual(result3, 0)
    
    def test_find_largest_empty_input(self):
        self.assertIsNone(find_largest([]))

    def test_find_largest_invalid_input(self):
        self.assertRaises(TypeError, find_largest, ['a', 'b', 'c'], msg="All elements in the list must be numbers")
        self.assertRaises(TypeError, find_largest, [1, 2, "3", 5], msg="All elements in the list must be numbers")
        self.assertRaises(TypeError, find_largest, [None, None], msg="nput must be a list")

if __name__ == "__main__":
    unittest.main()