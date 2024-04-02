def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all numbers in the range [low, high] that are
    divisible by one or more of the factors.
    >>> sum_multiples(1, 6, [3, 5])
    15
    >>> sum_multiples(1, 6, [4, 6])
    16
    >>> sum_multiples(1, 6, [4, 7])
    15
    """
    total = 0
    for i in range(low, high + 1):
        for j in factors:
            if i % j == 0:
                total += i
                break
    return total


def sum_below(n: int):
    """Return the sum of the integers below n.
    >>> sum_below(5)
    10
    >>> sum_below(10)
    35
    
	Include these tokens in the code:
	return 0
	if n < 0
	total += n
	n -= 1
	"""
    total = 0
    for i in range(n):
        total += i + 1
    return total


def factorial(n: int):
    """Return n factorial.
    >>> factorial(4)
    24
    >>> factorial(1)
    1
    >>> factorial(6)
    720
    >>> factorial(3)
    6
    """
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def count_down(x: int):
    """Print and count down from x to 0.
    >>> count_down(5)
    5
    4
    3
    2
    1
    0
    """
    for i in range(x, -1, -1):
        print(i)


def count_from(x: int):
    """