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
            continue
        return False
    return True


def sum_multiples(m: int, n: int, threshold: int) -> int:
    """Return the sum of all positive integers n <= threshold such that n is divisible by m and n + m is divisible by n.
    >>> sum_multiples(3, 5, 10)
    30
    >>> sum_multiples(5, 2, 25)
    20
    >>> sum_multiples(7, 2, 15)
    0
    """
    sum = 0
    for x in range(threshold):
        if x % m == 0 and (x + m) % n == 0:
            sum += x
    return sum


def sum_multiples_below(m: int, n: int, threshold: int) -> int:
    """Return the sum of all positive integers n <= threshold such that n is divisible by m and n + m is divisible by n.
    >>> sum_multiples_below(3, 5, 10)
    30
    >>> sum_multiples_below(5, 2, 25)
    20
    >>> sum_multiples_below(7, 2, 15)
    0
    """
    sum = 0
    for x in range(threshold):
        if x % m == 0 and (x + m) % n == 0:
            sum += x
    return sum


def sum_divisible(n: int, threshold: int) -> int:
    """Return the sum of all positive integers i <= threshold such that n divides i + n.
    >>> sum_divisible(3, 5)
    3
    >>> sum_divisible(5, 5)
    5
    >>> sum_divisible(7, 30)
    35
    """
    sum = 0
    for x in range(threshold):
        if (x + n) % n == 0:
            sum += x
   