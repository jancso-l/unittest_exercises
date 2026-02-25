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

def calculate_shipping_cost(weight, destination):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if not isinstance(destination, str):
        raise TypeError("Destination must be a string")
    if not destination:
        raise ValueError("Destination cannot be empty")
    if destination.lower() == "usa":
        return 0
    if destination.lower() == "canada":
        return weight * 1.5
    if destination.lower() == "mexico":
        return weight * 2.0
    return weight * 5.0

class TestCalculateShippingCost(unittest.TestCase):
    def test_non_numeric_weight(self):
        with self.assertRaises(ValueError, msg="Weight must be a number"):
            calculate_shipping_cost("5", "USA")
            

if __name__ == "__main__":
    unittest.main()

