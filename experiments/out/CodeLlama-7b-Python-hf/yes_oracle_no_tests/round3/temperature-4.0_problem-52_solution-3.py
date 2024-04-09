def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: print ( below _ th reshold ([ 1 ,
	"""

    return all(x < t for x in l)


def sum_of_digits(n: int) -> int:
    """Return the sum of the digits of n.

    >>> sum_of_digits(10) # 1 + 0 = 1
    1
    >>> sum_of_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_of_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    return sum(int(x) for x in str(n))


def last_digit_of(n: int) -> int:
    """Return the last digit of n.

    >>> last_digit_of(3) # 3
    3
    >>> last_digit_of(333) # 3
    3
    >>> last_digit_of(12345) # 5
    5
    >>> last_digit_of(1234567890) # 0
    0
    """
    "*** YOUR CODE HERE ***"
    return int(str(n)[-1])


def count_evens(nums: list) -> int:
    """Return the number of even numbers in the given list.

    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    "*** YOUR CODE HERE ***"
    return len([x for x in nums if x % 2 == 0])


def make_array(size: int) -> list:
    """Return a list of the given size, containing the first size numbers
    in the Fibonacci sequence (starting with 0 and 1), for example:
    make_array(5) --> [0, 1, 1, 2, 3]
    >>> make_array