def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x )
	"""
    # BEGIN PROBLEM 1
    s = str(x)
    if shift >= len(s):
        return s[::-1]
    else:
        return s[shift:] + s[:shift]
    # END PROBLEM 1


def circular_sort(x):
    """Return a number with the same digits as x, sorted from least to greatest.
    If x is sorted already, return x.
    >>> circular_sort(123)
    123
    >>> circular_sort(231)
    123
    """
    # BEGIN PROBLEM 2
    s = str(x)
    if s == ''.join(sorted(s)):
        return x
    else:
        return int(''.join(sorted(s)))
    # END PROBLEM 2


def is_palindrome(text):
    """Returns True if text is a palindrome and False otherwise.
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    >>> is_palindrome('tacocat')
    True
    """
    # BEGIN PROBLEM 3
    # BEGIN HELPER 1
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    # END HELPER 1
    return is_pal(str(text))
    # END PROBLEM 3


def is_pangram(text):
    """Returns True if text is a pangram and False otherwise.
    A pangram is a sentence that contains every letter of the alphabet at least once.
    >>> is_pangram('antartica')
    True
    >>> is_pangram('blueberry')
    False
    >>> is_pangram('Sudoku')
    True
    """
    # BEGIN PROBLEM 4
