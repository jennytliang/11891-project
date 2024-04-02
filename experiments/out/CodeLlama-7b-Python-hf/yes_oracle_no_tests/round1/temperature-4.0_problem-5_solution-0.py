from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res = []
	"""
    res = []
    for i in range(len(numbers) - 1):
        res.append(numbers[i])
        res.append(delimeter)
    res.append(numbers[-1])
    return res


def is_palindrome(s: str) -> bool:
    """Returns True if `s' is a palindrome, False otherwise.
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcb')
    False
    >>> is_palindrome('aabbcc')
    False
    >>> is_palindrome('aabbccbbaa')
    True
    """
    return s == s[::-1]
