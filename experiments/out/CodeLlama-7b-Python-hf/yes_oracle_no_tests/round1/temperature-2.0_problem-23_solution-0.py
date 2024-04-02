def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return len(stri)


def count_digits(n: int) -> int:
    """ Return the number of digits in the given integer
    >>> count_digits(123)
    3
    >>> count_digits(45678)
    5
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """

    return len(str(n))


def count_divisible(n: int) -> int:
    """ Return the number of numbers from 0 to n that are divisible by 7
    >>> count_divisible(100)
    14
    >>> count_divisible(20000)
    2857
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """

    count = 0
    for i in range(n + 1):
        if i % 7 == 0:
            count += 1
    return count


def sum_digits(n: int) -> int:
    """ Return the sum of the digits in the given integer
    >>> sum_digits(123)
    6
    >>> sum_digits(45678)
    26
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """

    return sum(int(i) for i in str(n))


def count_up_to(n: int) -> int:
    """ Return the number of numbers from 0 to n
    >>> count_up_to(100)
    101
    >>> count_up_to(100000)
    100001
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """

    return n + 1


def count_down_from(n: int) -> int:
    """ Return the number of numbers from n to 0
    >>> count_down_from(100)
    101
    >>> count_down_