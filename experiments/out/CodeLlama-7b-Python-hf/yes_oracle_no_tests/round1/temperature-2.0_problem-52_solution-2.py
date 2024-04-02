def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x < t:
            return True
        else:
            return False


def sum_multiples(n: int, high: int):
    """Return the sum of all positive multiples of n below high.
    >>> sum_multiples(3, 5)
    3
    >>> sum_multiples(3, 15)
    24
    >>> sum_multiples(5, 50)
    250
    >>> sum_multiples(3, 2)
    0
    >>> sum_multiples(3, 1)
    0
    """
    total = 0
    for i in range(high // n):
        total += (i + 1) * n
    return total


def sum_divisible_by(n: int, high: int):
    """Return the sum of all positive numbers less than high
    evenly divisible by n.
    >>> sum_divisible_by(4, 20)
    0
    >>> sum_divisible_by(5, 20)
    10
    >>> sum_divisible_by(3, 20)
    30
    >>> sum_divisible_by(6, 20)
    15
    >>> sum_divisible_by(2, 20)
    10
    >>> sum_divisible_by(7, 14)
    0
    >>> sum_divisible_by(3, 14)
    10
    >>> sum_divisible_by(2, 14)
    4
    """
    total = 0
    for i in range(1, high // n):
        if i % n == 0:
            total += i
    return total


def sum_divisible_by_two_up_to(n: int):
    """Return the sum of all positive numbers less than n
    evenly divisible by 2.
    >>> sum_divisible_by_two_up_to(20)
    20
    >>>