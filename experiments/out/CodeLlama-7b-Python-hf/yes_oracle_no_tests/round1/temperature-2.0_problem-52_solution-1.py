def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    for x in l:
        if x < t:
            return True
        else:
            return False


def sum_multiples(m: int, n: int, thresh: int):
    """Return the sum of multiples of m and n that are less than or equal to
    thresh.
	
    >>> sum_multiples(3, 5, 100)
    99
    >>> sum_multiples(3, 5, 8)
    18
    >>> sum_multiples(3, 5, 7)
    15
    >>> sum_multiples(3, 5, 6)
    12
    >>> sum_multiples(3, 5, 1)
    3
    >>> sum_multiples(3, 5, 0)
    0
    
	Include these tokens in the code: return all (m * x + n * y <= thresh
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    total = 0
    for x in range(thresh):
        for y in range(thresh):
            if x % m == 0 and y % n == 0:
                total += x * m + y * n
    return total


def sum_multiples_ii(m: int, n: int, thresh: int):
    """Return the sum of multiples of m and n that are less than or equal to
    thresh.
	
    >>> sum_multiples(3, 5, 100)
    99
    >>> sum_multiples(3, 5, 8)
    18
    >>> sum_multiples(3, 5, 7)
    15
    >>> sum_multiples(3, 5, 6)
    12
    >>> sum_multiples(3, 5, 1)
    3
    >>> sum_multiples(3, 5, 0)
    0
    
	Include these tokens in the code: return all (m * x + n * y <= thresh
	Do not include these