import unittest

# python -m unittest -v exercise4.TestContainer.test_container_has_code_attributee

# skipping tests:


# class Container:
#     code = 'ABCD1234'


# class TestContainer(unittest.TestCase):
#     def test_container_is_instance_of_type(self) -> None:
#         self.assertIsInstance(Container, type)

#     @unittest.skip("The container class requires implementation")
#     def test_container_has_code_attribute(self) -> None:
#         msg = 'The Container class does not have a code attribute.'
#         self.assertTrue(hasattr(Container, 'code'), msg)

# from datetime import date

# class Container:
#     def __init__(self):
#         if date.today().day % 2 == 0:
#             self.code = 'XC-0'
#         else:
#             self.code = 'XC-1'


# class TestContainer(unittest.TestCase):
#     @unittest.skipIf(date.today().day % 2 == 0, 'Skipping even days.')
#     def test_code_ends_with_0_on_even_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('0'), 'Expected code to end with 0.'
#         )
#     @unittest.skipIf(date.today().day % 2 == 1, 'Skipping odd days.')
#     def test_code_ends_with_1_on_odd_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('1'), 'Expected code to end with 1.'
#         )

# import sys

# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(sys.platform.startswith("win"), 'Requires Windows.')
#     def test_code_is_XC_win_on_Windows(self):
#         c = Container()
#         self.assertEqual(c.code, 'XC-win', 'Expected code to be XC-win.')

#     @unittest.skipUnless(sys.platform.startswith("linux", 'Requires Linux.'))
#     def test_code_starts_with_XC_on_Linux(self):
#         c = Container()
#         self.assertEqual(
#             c.code, 'XC-linux', 'Expected code to be XC-linux.'
#         )

# class EmailSender:
#     def send_email(self, to, subject, body):
#         # Code to send email
#         return True

# def is_network_available():
#     # Code to check if network is available 
#     return True

# class TestEmailSender(unittest.TestCase):
#     @unittest.skipIf(not is_network_available(), "Network unavailable")
#     def test_send_email(self):
#         self.assertTrue(EmailSender().send_email("Paul", "Question", "How are you?"))

# import os

# class FileReader:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_data(self):
#         with open(self.filename, 'r') as f:
#             return f.read()

# class TestFileReader(unittest.TestCase):
#     @unittest.skipUnless("test.txt" is None, "File not found")
#     def test_read_data(self):
#         document = FileReader("test.txt")
#         text = document.read_data()
#         self.assertIsNotNone(text)

# class DataTransformer:
#     def transform(self, data):
#         # Code to transform data
#         return transformed_data

# class TestDataTransformer(unittest.TestCase):
#     @unittest.skip("Test skipped as not implemented yet")
#     def test_transform(self):
#         self.fail("Test not implemented yet")

# class PaymentGateway:
#     def process_payment(self, amount):
#         # Code to process payment
#         return True


# def is_production_environment():
#     # Code to check if it is a production environment
#     return True

# class TestPaymentGateway(unittest.TestCase):
#     @unittest.skipIf(not is_production_environment(), "Not in production environment")
#     def test_process_payment(self):
#         self.assertTrue(PaymentGateway().process_payment(40))

import sys

# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(container.code, 'XC-linux')

# def setUpModule():
#     global container
#     container = Container() 

# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(container.code, 'XC-linux')

# ----------------------------------------------------------------
# Test fixtures

# def setUpModule():
#     global container
#     container = Container()

# def tearDownModule():
#     global container
#     del container

# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     # Enter your solution here
#     @classmethod
#     def setUpClass(cls):
#         cls.container = Container()

#     @classmethod
#     def tearDownClass(cls):
#         del cls.container

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         # code to remove
#         self.assertEqual(
#             self.container.code, 'XC-win'
#         )  # Code to modify

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         # code to remove
#         self.assertEqual(
#             self.container.code, 'XC-linux'
#         )  # Code to modify

# class Container:
#     def __init__(self, category):
#         self.category = category

#     def __repr__(self):
#         return f"Container(category='{self.category}')"


# class TestContainer(unittest.TestCase):
#     # Enter your solution here
#     def setUp(self):
#         self.container = Container("plastic")
    
#     def tearDown(self):
#         del self.container

#     def test_init_method(self):
#         #container = Container('plastic')  # Remove this code
#         msg = (
#             'The container instance does not have a category '
#             'attribute.'
#         )
#         self.assertTrue(
#             hasattr(self.container, 'category'), msg
#         )  # Modify this code
#         self.assertEqual(
#             self.container.category, 'plastic'
#         )  # Modify this code

#     def test_repr_method(self):
#         #container = Container('plastic')  # remove this
#         self.assertEqual(
#             repr(self.container), "Container(category='plastic')"
#         )  # Modify this code

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def tearDown(self):
        del self.calculator
    
    def test_add(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = self.calculator.subtract(10, 2)
        self.assertEqual(result, 8)
    

if __name__ == "__main__":
    unittest.main()

