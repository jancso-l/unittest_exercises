import unittest
import math

# Function testing

# def circle_area(radius):
#     """Calculate the area of a circle given its radius."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('Radius must be of type int or float.')

#     if not radius > 0:
#         raise ValueError('Radius must be positive.')

#     return math.pi * radius ** 2

# class TestCircleArea(unittest.TestCase):
#     def test_area_with_radius_one(self):
#         result = circle_area(1)
#         self.assertAlmostEqual(result, math.pi, places=5)

#     def test_area_with_radius_three(self):
#         result = circle_area(3)
#         self.assertAlmostEqual(result, math.pi*9, places=5)
    
#     def test_incorrect_type(self):
#         self.assertRaises(TypeError, circle_area, "4")
#         self.assertRaises(TypeError, circle_area, None)
    
#     def test_incorrect_value(self):
#         self.assertRaises(ValueError, circle_area, 0)
#         self.assertRaises(ValueError, circle_area, -3)

# def perimeter(radius):
#     """The function returns the length of the circle."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('The radius must be of type int or float.')

#     if radius <= 0:
#         raise ValueError('The radius must be positive.')

#     return 2 * math.pi * radius

# class TestPerimeter(unittest.TestCase):
#     def test_correct_perimeter_five(self):
#         expected = perimeter(5)
#         self.assertAlmostEqual(expected, 31.4159, places=4)

#     def test_correct_perimeter_one(self):
#         expected = perimeter(1)
#         self.assertAlmostEqual(expected, 6.2831, places=3)
    
#     def test_incorrect_type(self):
#         with self.assertRaises(TypeError):
#             perimeter("Bob")
#         with self.assertRaises(TypeError):
#             perimeter([1,2,3])
    
#     def test_incorrect_value(self):
#         self.assertRaises(ValueError, perimeter, -10.25)
#         self.assertRaises(ValueError, perimeter, -0)

# from tax import calculate_tax

# class TestCalculateTax(unittest.TestCase):
#     def test_tax_with_eighteen_age(self):
#         expected = calculate_tax(60000, 18)
#         self.assertEqual(expected, 6000)
    
#     def test_tax_with_nineteen_age(self):
#         expected = calculate_tax(60000, 19)
#         self.assertEqual(expected, 10200)

#     def test_tax_with_sixty_five_age(self):
#         expected = calculate_tax(60000, 65)
#         self.assertEqual(expected, 10200)

#     def test_tax_with_sixty_six_age(self):
#         expected = calculate_tax(60000, 66)
#         self.assertEqual(expected, 9000)       

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# class TestIsEven(unittest.TestCase):
#     def test_even_numbers(self):
#         self.assertTrue(is_even(10))
#         self.assertTrue(is_even(100))
    
#     def test_odd_numbers(self):
#         self.assertFalse(is_even(13))
#         self.assertFalse(is_even(131))

# def factorial(num):
#     if num < 0:
#         raise ValueError
#     elif num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
    
# class TestFactorial(unittest.TestCase):
#     def test_factorial_zero(self):
#         self.assertEqual(factorial(0), 1)

#     def test_factorial_positive(self):
#         self.assertEqual(factorial(5), 120)

#     def test_factorial_negative(self):
#         self.assertRaises(ValueError, factorial, -5)   

# def calculate(numbers, operation):
#     if not isinstance(numbers, list):
#         raise TypeError("First argument must be a list of numbers")
#     if not isinstance(operation, str) or operation not in [
#         "+",
#         "-",
#         "*",
#         "/",
#     ]:
#         raise ValueError(
#             "Second argument must be a string representing"
#             "a valid operation (+, -, *, /)"
#         )
#     if operation == "+":
#         return sum(numbers)
#     elif operation == "-":
#         return numbers[0] - sum(numbers[1:])
#     elif operation == "*":
#         result = 1
#         for num in numbers:
#             result *= num
#         return result
#     elif operation == "/":
#         if 0 in numbers:
#             raise ZeroDivisionError("Cannot divide by zero")
#         result = numbers[0]
#         for num in numbers[1:]:
#             result /= num
#         return result

# class TestCalculate(unittest.TestCase):
#     def test_raises_type_error_if_first_arg_not_list(self):
#         with self.assertRaises(TypeError):
#             calculate(5, "+")
    
#     def test_raises_value_error_if_second_arg_not_valid_operation(self):
#         with self.assertRaises(ValueError):
#             calculate([1, 2, 3], "Bob")
    
#     def test_performs_addition_correctly(self):
#         expected = calculate([1,2,3], "+")
#         self.assertEqual(expected, 6)
    
#     def test_performs_subtraction_correctly(self):
#         expected = calculate([3,2,1], "-")
#         self.assertEqual(expected, 0)

#     def test_performs_multiplication_correctly(self):
#         expected = calculate([1,2,3], "*")
#         self.assertEqual(expected, 6)
    
#     def test_performs_division_correctly(self):
#         expected = calculate([12,4,3], "/")
#         self.assertEqual(expected, 1)
    
#     def test_raises_zero_division_error_if_dividing_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             calculate([12, 0, 3], "/")

# def is_valid_password(password):
#     if len(password) < 8:
#         return False
#     if not any(c.isdigit() for c in password):
#         return False
#     if not any(c.isupper() for c in password):
#         return False
#     if not any(c.islower() for c in password):
#         return False
#     return True

# class TestIsValidPassword(unittest.TestCase):
#     def test_is_valid_password_valid(self):
#         self.assertTrue(is_valid_password("Password21"))

#     def test_is_valid_password_short(self):
#         self.assertFalse(is_valid_password("Passwo"))
    
#     def test_is_valid_password_no_digits(self):
#         self.assertFalse(is_valid_password("PasswordPassword"))

#     def test_is_valid_password_no_uppercase(self):
#         self.assertFalse(is_valid_password("password21"))
    
#     def test_is_valid_password_no_lowercase(self):
#         self.assertFalse(is_valid_password("PASSWORD21"))

# -------------------------------------------------------------------
# Class testing

# from src.tax1 import SimpleTaxCalculator

# class TestIncomeTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()

#     def test_income_tax_below_threshold(self):
#         self.assertEqual(self.calc.income_tax(60000), 10200)

#     def test_income_tax_equal_threshold(self):
#         self.assertEqual(self.calc.income_tax(85528), 14539.76)

#     def test_income_tax_above_threshold(self):
#         self.assertEqual(self.calc.income_tax(100000), 19170.8)

# from src.tax2 import SimpleTaxCalculator

# class TestVatTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()
    
#     def test_vat_tax_with_zero_price(self):
#         self.assertEqual(self.calc.vat_tax(0), 0)

#     def test_vat_tax_with_zero_price(self):
#         self.assertEqual(self.calc.vat_tax(float('inf')), float('inf'))

#     def test_vat_tax_with_string_input(self):
#         self.assertRaises(TypeError, self.calc.vat_tax, "Bob")

# class TestCapitalGainsTax(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.calc = SimpleTaxCalculator()
    
#     def test_capital_gains_tax_with_positive_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(1000), 190)

#     def test_capital_gains_tax_with_zero_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(0), 0)

#     def test_capital_gains_tax_with_negative_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(-100), 0)

#     def test_capital_gains_tax_with_large_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(1000000), 190000)

#     def test_capital_gains_tax_with_float_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(50.0), 9.5)

#     def test_capital_gains_tax_with_max_float_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(float("inf")), float("inf"))

#     def test_capital_gains_tax_with_string_profit(self):
#         self.assertRaises(TypeError, self.calc.capital_gains_tax, "1000")

#     def test_capital_gains_tax_with_none_profit(self):
#         self.assertRaises(TypeError, self.calc.capital_gains_tax, None)

# def setUpModule():
#     global calc
#     calc = SimpleTaxCalculator()

# from src.emp import Employee

# class TestEmployee(unittest.TestCase):

#     def setUp(self):
#         self.emp = Employee("John", "Smith", 40, 80000)

#     def test_email(self):
#         expected = self.emp.email
#         self.assertEqual(expected, 'john.smith@mail.com')

#     # def test_email_after_changing_first_name(self):
#     #     self.emp.first_name = "Mike"
#     #     self.assertEqual(self.emp.email, 'mike.smith@mail.com')

#     def test_email_after_changing_last_name(self):
#         self.emp.last_name = "Doe"
#         self.assertEqual(self.emp.email, 'john.doe@mail.com')

# from src.emp1 import Employee

# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)
    
#     def test_get_salary(self):
#         self.assertEqual(self.emp.salary, 80000)

#     def test_apply_bonus(self):
#         self.emp.apply_bonus()
#         self.assertEqual(self.emp.salary, 88000)

# from src.notebook import Note

# class TestNote(unittest.TestCase):
#     def setUp(self):
#         self.note = Note('Simple note.')

#     # def test_note_has_content_instance_attr(self):
#     #     self.assertHasAttr(self.note, "content", msg='A Note instance does not have a content attribute.')

#     def test_note_has_category_class_attr(self):
#         self.assertHasAttr(self.note, "CATEGORY", 'The Note class does not have a CATEGORY attribute.')

# from src.notebook1 import Notebook

# class TestNotebook(unittest.TestCase):
#     def setUp(self):
#         self.notebook = Notebook()
#         self.notebook.add_note('Big Data')
#         self.notebook.add_note('Data Science')
#         self.notebook.add_note('Machine Learning')

#     def test_search_notes_method(self):
#         self.assertEqual(self.notebook.search_notes("data"), ['Big Data', 'Data Science'])


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

# class TestShoppingCart(unittest.TestCase):
#     cart = ShoppingCart()

#     def test_add_remove_item(self):
#         self.cart.add_item("milk")
#         self.assertIn("milk", self.cart.items)
#         self.cart.add_item("bread")
#         self.assertIn("bread", self.cart.items)
#         self.assertEqual(self.cart.items, ["milk", "bread"])
#         self.cart.remove_item("milk")
#         self.assertNotIn("milk", self.cart.items)
#         self.cart.remove_item("bread")
#         self.assertNotIn("bread", self.cart.items)
#         self.assertEqual(len(self.cart.items), 0)

from src.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Joe", 32, "male")
        self.person2 = Person("Kate", 22, "female")

    def test_person_attributes(self):
        self.assertHasAttr(self.person1, "name")
        self.assertHasAttr(self.person1, "age")
        self.assertHasAttr(self.person1, "gender")

        self.assertHasAttr(self.person2, "name")
        self.assertHasAttr(self.person2, "age")
        self.assertHasAttr(self.person2, "gender")

        self.assertEqual(self.person1.name, "Joe")
        self.assertEqual(self.person2.gender, "female")
    
    def test_person_str_method(self):
        self.assertEqual(self.person1.__str__(), "Joe (32, male)")
        self.assertEqual(self.person2.__str__(), "Kate (22, female)")

        


if __name__ == "__main__":
    unittest.main()