def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return True if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abbcba')
    True
    """
    return string == string[::-1]


def list_prod(nums: list) -> int:
    """ Return product of all items in list
    >>> list_prod([1, 2, 3])
    6
    >>> list_prod([1, 2, 3, 4])
    24
    """
    return 1 if len(nums) == 0 else nums[0] * list_prod(nums[1:])


def list_sum(nums: list) -> int:
    """ Return sum of all items in list
    >>> list_sum([1, 2, 3])
    6
    >>> list_sum([1, 2, 3, 4])
    10
    """
    return 0 if len(nums) == 0 else nums[0] + list_sum(nums[1:])


def list_reverse(nums: list) -> list:
    """ Return reverse of given list
    >>> list_reverse([1, 2, 3])
    [3, 2, 1]
    >>> list_reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return nums[::-1]


def is_prime(num: int) -> bool:
    """ Return True if given number is prime
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    """
    return num > 1 and all(num % i for i in range(2, num))


def first_n_primes(n: int) -> list:
    """ Return