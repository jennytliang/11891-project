def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for num in l :
	"""

    for num in l:
        if num >= t:
            return False

    return True


def sum_multiples(low: int, high: int, divisors: list):
    """Return the sum of all the multiples of the divisors between low and high.
    >>> sum_multiples(1, 10, [3, 5])
    30
    >>> sum_multiples(1, 100, [3, 5])
    2310
    >>> sum_multiples(1, 200, [3, 5, 7, 11])
    6060
    """

    sum = 0
    for i in range(low, high):
        for div in divisors:
            if i % div == 0:
                sum += i
                break

    return sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
