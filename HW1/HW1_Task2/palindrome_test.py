import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("a man a plan a canal panama"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_numeric_palindrome(self):
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindrome_with_similar_letters(self):
        self.assertFalse(is_palindrome("abccbaa"))

if __name__ == '__main__':
    unittest.main()