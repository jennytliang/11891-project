from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: def main (): assert inter s per
	"""


    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i != len(numbers) - 1:
            res.append(delimeter)
    return res


def is_palindrome(str: str) -> bool:
    """Return True if string `str' is palindrome, otherwise return False.
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcbaX')
    False
    
	Do not include these tokens in the code: def main (): assert is palindrome
	"""


def get_largest_number(numbers: List[int]) -> int:
    """Return the largest number of input list `numbers'.
    >>> get_largest_number([1, 2, 3])
    3
    >>> get_largest_number([1, 2, 3, 2, 1])
    3
    >>> get_largest_number([1, 2, 3, 2, 1, 0])
    3
    >>> get_largest_number([1, 1, 1])
    1
    >>> get_largest_number([0])
    0
    >>> get_largest_number([1, -1, -1])
    1
    
	Do not include these tokens in the code: def main (): assert get largest number
	"""


def get_smallest_number(numbers: List[int]) -> int:
    """Return the smallest number of input list `numbers'.
    >>> get_smallest_number([1, 2, 3])
    1
    >>> get_smallest_number([1, 2, 3, 2, 1])
    1
    >>> get_smallest_number([1, 2, 3, 2, 1, 0])
    0
    >>> get_smallest_number([1, 1, 1])
    1
    >>> get_smallest_number([0])
    0
    >>> get_smallest_number([1, -1, -1])
    -1
    
