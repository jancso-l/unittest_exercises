# # Organizing tests in test suites

import unittest

# # 1:

# def calculate_rectangle_area(length, width):
#     return length * width

# def calculate_square_area(side_length):
#     return side_length ** 2

# class TestAreaFunctions(unittest.TestCase):
#     def test_rectangle_area(self):
#         self.assertEqual(calculate_rectangle_area(5, 10), 50)
#         self.assertEqual(calculate_rectangle_area(3, 4), 12)

#     def test_square_area(self):
#         self.assertEqual(calculate_square_area(5), 25)
#         self.assertEqual(calculate_square_area(2), 4)

# if __name__ == '__main__':

# # Task:  Create a TestSuite object and add these two test cases to it. Then, run the TestSuite to ensure that both functions pass their unit tests.

# # Create a test suite
#     suite = unittest.TestSuite()

# # Adding Test Cases to the Suite: 
#     suite.addTest(TestAreaFunctions("test_rectangle_area"))
#     suite.addTest(TestAreaFunctions("test_square_area"))

# # Create a test runner and run the suite
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# # -----------------------------------------------------------------------------
# 2:

# def reverse_string(string):
#     return string[::-1]


# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = ""
#     for letter in string:
#         if letter.lower() not in vowels:
#             result += letter
#     return result


# def capitalize_first_letter(string):
#     return string.capitalize()


# class TestStringManipulationFunctions(unittest.TestCase):
#     def test_reverse_string(self):
#         self.assertEqual(reverse_string('hello'), 'olleh')
#         self.assertEqual(reverse_string('world'), 'dlrow')

#     def test_remove_vowels(self):
#         self.assertEqual(remove_vowels('hello world'), 'hll wrld')
#         self.assertEqual(remove_vowels('python is awesome'), 'pythn s wsm')

#     def test_capitalize_first_letter(self):
#         self.assertEqual(capitalize_first_letter('hello'), 'Hello')
#         self.assertEqual(capitalize_first_letter('world'), 'World')

# # Task: Create a TestSuite object and add these three test cases to it. Then, run the TestSuite to ensure that both functions pass their unit tests.

# suite = unittest.TestSuite()
# suite.addTests([
#     TestStringManipulationFunctions("test_reverse_string"), 
#     TestStringManipulationFunctions("test_remove_vowels"),
#     TestStringManipulationFunctions("test_capitalize_first_letter")
#     ])

# runner = unittest.TextTestRunner()
# runner.run(suite)

# -------------------------------------------------------------
# 3:
# from src.test_arithmetic import TestAdditionAndSubtraction
# from src.test_arithmetic import TestMultiplicationAndDivision

# Your task is to organize these two classes into a test suite using the TestSuite class from the unittest module and run the given tests.

# suite = unittest.TestSuite()

# loader1 = unittest.TestLoader()
# suite1 = loader1.loadTestsFromTestCase(TestAdditionAndSubtraction)
# suite2 = loader1.loadTestsFromTestCase(TestMultiplicationAndDivision)

# suite1.addTest(suite2)

# suite3 = unittest.TestSuite([suite1, suite2])

# runner = unittest.TextTestRunner()
# runner.run(suite)

# -----------------------------------------------------------------
# 4:

# Your task is to organize these two classes into a test suite using the TestSuite class from the unittest module and run the given tests.

from src.test_animals import TestCats, TestDogs

loader = unittest.TestLoader()

suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromTestCase(TestCats))
suite.addTest(loader.loadTestsFromTestCase(TestDogs))

runner = unittest.TextTestRunner()

runner.run(suite)


