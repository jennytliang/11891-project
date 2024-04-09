from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: numbers )): res . append ( numbers [
	Do not include these tokens in the code: nu
	"""


    res = []
    for i in rang(len(numbers)):
        res.append(numbers[i])
        if (i < len(numbers) - 1):
            res.append(delimeter)
    return res


def delete_n(numbers: List[int], n: int) -> List[int]:
    """ Delete all elements from input list `numbers' that are equal to `n'
    >>> delete_n([1, 2, 3, 3, 3, 3], 3)
    [1, 2]
    """

    return list(filter(lambda x: x != n, numbers))


def is_palindrome(input_str: str) -> bool:
    """ Return True if input_str is a palindrome. Otherwise, return False.
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('aabb')
    False
    """

    return input_str == input_str[::-1]


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Return a list of unique elements from input list `numbers'
    >>> remove_duplicates([1, 1, 2, 3, 3])
    [1, 2, 3]
    """

    return list(set(numbers))


def is_unique(numbers: List[int]) -> bool:
    """ Return True if all elements of input list `numbers' are unique. Otherwise, return False.
    >>> is_unique([1, 2, 3, 4])
    True
    >>> is_unique([1, 2, 3, 4, 1])
    False
    """

    return len(numbers) == len(set(numbers))


def get_top_n(numbers: List[int], n: int) -> List[int]:
    """ Return a list of the top n elements from input list `numbers'.
    If `n' is greater than the length of `numbers', return `numbers'.
    >>> get_top_n([1, 2, 3, 4, 5], 2)
    [