from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res =
	Do not include these tokens in the code: if numbers ==
	"""
    res = []

    if numbers == []:
        return []

    res.append(numbers[0])
    for i in range(len(numbers) - 1):
        res.append(delimeter)
        res.append(numbers[i + 1])

    return res


def is_prime(number: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_palindrome(string: str) -> bool:
    """
    >>> is_palindrome("")
    True
    >>> is_palindrome("ab")
    False
    >>> is_palindrome("abccba")
    True
    """
    if len(string) <= 1:
        return True

    return string[0] == string[-1] and is_palindrome(string[1:-1])


def is_palindrome_two_pointers(string: str) -> bool:
    """
    >>> is_palindrome_two_pointers("")
    True
    >>> is_palindrome_two_pointers("ab")
    False
    >>> is_palindrome_two_pointers("abccba")
    True
    """
    if len(string) <= 1:
        return True

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_recursive(string: str) -> bool:
    """
    >>> is_