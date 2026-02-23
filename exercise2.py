import unittest

# def calculate_daily_return(
#     open_price: float, close_price: float
# ) -> float:
#     return round(((close_price / open_price) - 1) * 100, 2)


# class TestCalculateDailyReturn(unittest.TestCase):
#     def test_positive_return(self):
#         self.assertEqual(calculate_daily_return(349.0, 360.0), 3.15)
    
#     def test_negative_return(self):
#         self.assertEqual(calculate_daily_return(349.0, 340.0), -2.58)

#     def test_zero_return(self):
#         self.assertEqual(calculate_daily_return(349.0, 349.0), 0.0)

# class Doc:
#     def __init__(self, string: str) -> None:
#         self.string = string
        
#     def __repr__(self) -> str:
#         return f"Doc(string='{self.string}')"

#     def __lt__(self, other) -> bool:
#         return len(self.string) < len(other.string)

#     def __gt__(self, other) -> bool:
#         return len(self.string) > len(other.string)

# doc1 = Doc('Online')
# doc2 = Doc('Nature')
# doc3 = Doc('Technology')

# class TestDoc(unittest.TestCase):
#     # def test_less_than(self):
#     #     self.assertLess(doc2, doc1)
#     #     self.assertLess(doc3, doc1)
    
#     # def test_greater_than(self):
#     #     self.assertGreater(doc1, doc2)
#     #     self.assertGreater(doc1, doc3)
#     def test_equal(self):
#         self.assertEqual(doc1, doc2)

#     def test_not_equal(self):
#         self.assertNotEqual(doc3, doc1)
#         self.assertNotEqual(doc3, doc2)    

# class Employee:
#     """A simple class that describes an employee of the company."""

#     TAX_RATE = 0.17
#     BONUS_RATE = 0.10

#     def __init__(
#         self, first_name: str, last_name: str, salary: int
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def email(self) -> str:
#         return (
#             f'{self.first_name.lower()}.{self.last_name.lower()}'
#             '@mail.com'
#         )

#     @property
#     def tax(self) -> float:
#         return round(self.salary * self.TAX_RATE, 2)

#     def apply_bonus(self) -> None:
#         self.salary = int(self.salary * (1 + self.BONUS_RATE))

# class TestEmployee(unittest.TestCase):
#     def test_has_email_attr(self):
#         self.assertHasAttr(Employee, "email", msg='The Employee class does not have an email attribute.')
#     def test_has_tax_attr(self):
#         self.assertHasAttr(Employee, "tax", msg='The Employee class does not have a tax attribute.')
#     def test_has_apply_bonus(self):
#         self.assertHasAttr(Employee, "apply_bonus", msg='The Employee class does not have an apply_bonus attribute.')

# class TestEmployee(unittest.TestCase):
#     def test_has_email_attr(self):
#         self.assertHasAttr(Employee, "email", msg='The Employee class does not have an email attribute.')

#     def test_has_email_property(self):
#         self.assertIsInstance(Employee.email, property)

# class StringListOnly(list):
#     def append(self, string: str) -> None:
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)

# class TestStringListOnly(unittest.TestCase):
#     slo = StringListOnly()
    # def test_append_string(self):
    #     str_li = StringListOnly()
    #     str_li.append("I am a string")
    #     self.assertIn("I am a string", str_li)
    
    # def test_append_not_string_should_raise_error(self):
    #     str_li = StringListOnly()
    #     with self.assertRaises(TypeError):
    #         str_li.append(["I am a list"])
    #     self.assertRaises(TypeError,  str_li.append, True)

    # def test_slo_is_instance(self):
    #     self.assertIsInstance(self.slo, StringListOnly)
    #     self.assertIsInstance(self.slo, list)

# class Calculator:
#     def divide(self, dividend: float, divisor: float) -> float:
#         if divisor == 0:
#             raise ValueError("Cannot divide by zero")
#         return dividend / divisor

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         self.calculator = Calculator()

#     def test_divide_positive_numbers(self):
#         self.assertEqual(self.calculator.divide(6,3), 2)

#     def test_divide_zero_by_positive_number(self):
#         self.assertEqual(self.calculator.divide(0,3), 0)

#     def test_divide_negative_by_positive_number(self):
#         self.assertEqual(self.calculator.divide(-6, 3), -2)

#     def test_divide_by_zero_should_raise_error(self):
#         with self.assertRaises(ValueError):
#             self.calculator.divide(3, 0)

#     def tearDown(self):
#        del self.calculator

# def count_lines(filename: str) -> int:
#     try:
#         with open(filename, 'r') as f:
#             lines = f.readlines()
#             return len(lines)
#     except FileNotFoundError as e:
#         raise FileNotFoundError(f"File {filename} not found") from e
    
# class TestCountLines(unittest.TestCase):
#     def test_count_lines_of_existing_file(self):
#         self.assertEqual(count_lines("evaluate.py"), 21)

#     def test_count_lines_of_non_existing_file(self):
#         self.assertRaises(FileNotFoundError, count_lines, "non_existing_script.py")

def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)

class TestCalculateGrade(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(calculate_grade([10, 20, 30, 40]), 25)

if __name__ == "__main__":
    unittest.main()