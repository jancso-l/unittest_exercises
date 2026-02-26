import unittest


# def divide(x, y):
#     return x / y

# class TestDivide(unittest.TestCase):
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(6, 0)

# def calculate_discount(price, discount_rate):
#     if not isinstance(price, (int, float)):
#         raise TypeError("Price must be a number")
#     if not isinstance(discount_rate, (int, float)):
#         raise TypeError("Discount rate must be a number")
#     if price < 0 or discount_rate < 0:
#         raise ValueError(
#             "Price and discount rate must be non-negative"
#         )
#     discount = price * discount_rate
#     return price - discount

# class TestCalculateDiscount(unittest.TestCase):
#     def test_non_number_price(self):
#         self.assertRaises(TypeError, calculate_discount, ("price", 10.5))            
    
#     def test_negative_price(self):
#         with self.assertRaises(ValueError):
#             calculate_discount(-21, 2)

# def calculate_area(length, width):
#     if not isinstance(length, (int, float)):
#         raise TypeError("Length must be a number")
#     if not isinstance(width, (int, float)):
#         raise TypeError("Width must be a number")
#     if length <= 0 or width <= 0:
#         raise ValueError("Length and width must be positive")
#     return length * width

# class TestCalculateArea(unittest.TestCase):
#     def test_zero_values(self):
#         with self.assertRaises(ValueError):
#             calculate_area(0, 10)
#         with self.assertRaises(ValueError):
#             calculate_area(5, 0)
#         with self.assertRaises(ValueError):
#             calculate_area(0, 0)
    
#     def test_negative_values(self):
#         with self.assertRaises(ValueError):
#             calculate_area(-5, -10)
    
#     def test_non_number_values(self):
#         self.assertRaises(TypeError, calculate_area, ("length", "width"))

# def find_longest_word(words):
#     if not isinstance(words, list):
#         raise TypeError("Input must be a list")
#     if not all(isinstance(word, str) for word in words):
#         raise TypeError("List must contain only strings")
#     if not words:
#         raise ValueError("List cannot be empty")
#     return max(words, key=len)

# class TestFindLongestWord(unittest.TestCase):
#     def test_empty_list(self):
#         with self.assertRaises(ValueError):
#             find_longest_word([])
    
#     def test_non_string_elements(self):
#         with self.assertRaises(TypeError):
#             find_longest_word("list")
#         with self.assertRaises(TypeError):
#             find_longest_word([1, 2, 3])
#         with self.assertRaises(TypeError):
#             find_longest_word(["hyppopotamus", 2, "arachnophobia"])

# def get_average_grade(grades):
#     if not isinstance(grades, dict):
#         raise TypeError("Input must be a dictionary")
#     if not all(isinstance(key, str) for key in grades.keys()):
#         raise TypeError("Keys must be strings")
#     if not all(
#         isinstance(value, (int, float)) for value in grades.values()
#     ):
#         raise TypeError("Values must be numbers")
#     if not grades:
#         raise ValueError("Dictionary cannot be empty")
#     return sum(grades.values()) / len(grades)

# class TestGetAverageGrade(unittest.TestCase):
#     def test_empty_dict(self):
#         with self.assertRaises(ValueError):
#             get_average_grade({})
    
#     def test_non_string_keys(self):
#         with self.assertRaises(TypeError):
#             get_average_grade({True: 2, False: 5})
#         with self.assertRaises(TypeError):
#             get_average_grade({3: 2, 4: 5})
    
#     def test_non_numeric_values(self):
#         with self.assertRaises(TypeError):
#             get_average_grade({"Alice": "Bob", "Charlie": "David"})
#         with self.assertRaises(TypeError):
#             get_average_grade({"Alice": [1,2,3], "Charlie": (2,3,4)})

# def calculate_shipping_cost(weight, destination):
#     if not isinstance(weight, (int, float)):
#         raise TypeError("Weight must be a number")
#     if weight <= 0:
#         raise ValueError("Weight must be greater than zero")
#     if not isinstance(destination, str):
#         raise TypeError("Destination must be a string")
#     if not destination:
#         raise ValueError("Destination cannot be empty")
#     if destination.lower() == "usa":
#         return 0
#     if destination.lower() == "canada":
#         return weight * 1.5
#     if destination.lower() == "mexico":
#         return weight * 2.0
#     return weight * 5.0

# class TestCalculateShippingCost(unittest.TestCase):
#     def test_non_numeric_weight(self):
#         with self.assertRaisesRegex(TypeError,  "Weight must be a number"):
#             calculate_shipping_cost("LOL", "California")
    
#     def test_non_positive_weight(self):
#         with self.assertRaisesRegex(ValueError, "Weight must be greater than zero"):
#             calculate_shipping_cost(-20, "California")
    
#     def test_non_string_destination(self):
#         with self.assertRaisesRegex(TypeError, "Destination must be a string"):
#             calculate_shipping_cost(100, 100)

#     def test_empty_destination(self):
#         with self.assertRaisesRegex(ValueError, "Destination cannot be empty"):
#             calculate_shipping_cost(100, "")

# def calculate_grade(scores):
#     if not isinstance(scores, list):
#         raise TypeError("Input must be a list")
#     if not scores:
#         raise ValueError("List cannot be empty")
#     if not all(isinstance(score, (int, float)) for score in scores):
#         raise TypeError("Elements of list must be numbers")
#     if not all(0 <= score <= 100 for score in scores):
#         raise ValueError("Elements of list must be between 0 and 100")
#     return sum(scores) / len(scores)

# class TestCalculateGrade(unittest.TestCase):
#     def test_non_list_input(self):
#         with self.assertRaisesRegex(TypeError, "Input must be a list"):
#             calculate_grade(5)
    
#     def test_empty_list_input(self):
#         with self.assertRaisesRegex(ValueError, "List cannot be empty"):
#             calculate_grade([])
    
#     def test_non_numeric_element(self):
#         with self.assertRaisesRegex(TypeError, "Elements of list must be numbers"):
#             calculate_grade([1,2, "A", 'B', 5])
    
#     def test_out_of_range_element(self):
#         with self.assertRaisesRegex(ValueError,  "Elements of list must be between 0 and 100"):
#             calculate_grade([1,2,3, -10, 102])

import warnings

# def calculate_salary(wages, hours):
#     if len(wages) != len(hours):
#         raise ValueError("Wages and hours lists must have the same length")
#     if not all(isinstance(wage, (int, float)) for wage in wages):
#         raise TypeError("Wages list must contain numbers")
#     if not all(isinstance(hour, (int, float)) for hour in hours):
#         raise TypeError("Hours list must contain numbers")
#     if not all(hour >= 0 for hour in hours):
#         raise ValueError("Hours must be non-negative")
#     if not all(wage >= 0 for wage in wages):
#         raise ValueError("Wages must be non-negative")
#     total_salary = sum([wages[i]*hours[i] for i in range(len(wages))])
#     if total_salary == 0:
#         warnings.warn("Total salary is zero or negative")
#     return total_salary

# class TestCalculateSalary(unittest.TestCase):
#     def test_zero_salary_warning(self):
#         with self.assertWarns(UserWarning, msg="Total salary is zero or negative"):
#             calculate_salary([0],[0])

class User:
    def __init__(self, password):
        self.password = password
        if len(password) < 8:
            warnings.warn("Password too short", category=Warning)

class TestUser(unittest.TestCase):
    def test_short_password_warning(self):
        with self.assertWarns(Warning, msg="Password too short"):
            user = User("passwor") 
            print(user.password)       
            self.assertIsNotNone(user.password)

            user1 = User("password")
            self.assertGreaterEqual(len(user1.password), 8)

if __name__ == "__main__":
    unittest.main()
