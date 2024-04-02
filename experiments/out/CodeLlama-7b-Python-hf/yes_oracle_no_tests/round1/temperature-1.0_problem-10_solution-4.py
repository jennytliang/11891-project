def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    # TODO: implement longest palindrome algorithm from the lecture.
    pass


import unittest
import itertools


class IsPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            ('', True),
            ('a', True),
            ('ab', False),
            ('aba', True),
            ('abba', True),
            ('abcdef', False),
            ('bccbd', True),
        ]

    def test(self):
        for param, expected in self.test_data:
            msg = 'expected {0}, got {1} for {2}'.format(expected, is_palindrome(param), param)
            self.assertEqual(expected, is_palindrome(param), msg)


class MakePalindromeTest(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            ('', ''),
            ('a', 'a'),
            ('abba', 'abba'),
            ('cat', 'catac'),
            ('cata', 'catac'),
            ('cabbac', 'cabbac')
        ]

    def test(self):
        for param, expected in self.test_data:
            self.assertEqual(expected, make_palindrome(param), "expected {0}, got {1} for {2}".format(expected, make_palindrome(param), param))


if __name__ == '__main__':
    unittest.main()
