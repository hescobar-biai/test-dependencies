import unittest
from src.demo.functions import return_text, return_number

class TestDemoFunctions(unittest.TestCase):
    def test_return_text(self):
        """Test that return_text returns the expected string."""
        self.assertEqual(return_text(), "Hello, this is a text message from the demo!")

    def test_return_number(self):
        """Test that return_number returns the expected number."""
        self.assertEqual(return_number(), 42)

    def test_return_number_float(self):
        """Test that return_number returns the expected number."""
        self.assertEqual(test_return_number_float(), 42.5)

if __name__ == '__main__':
    unittest.main()
