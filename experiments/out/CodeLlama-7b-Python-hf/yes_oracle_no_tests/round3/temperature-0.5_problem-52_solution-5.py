def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return all(x < t for x i l)


def squares(s: set):
    """Return a new set of all squares of numbers in set s.

    >>> squares({1, 3, 15})
    {1, 9, 25}
    >>> squares(set())
    set()
    """


    return {x * x for x in s}


def convert_to_base(n: int, base: int):
    """Return a string representing the number n in base base.
    >>> convert_to_base(32, 2)
    '100000'
    >>> convert_to_base(32, 4)
    '30'
    >>> convert_to_base(32, 16)
    '20'
    """


    if n == 0:
        return '0'
    digits = ''
    while n > 0:
        digits += str(n % base)
        n //= base
    return digits[::-1]


def is_prime(n: int):
    """Returns True if n is a prime number.
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(521)
    True
    """


    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_divisors(n: int):
    """Returns the number of divisors of n.
    >>> count_divisors(20)
    4
    >>> count_divisors(25)
    6
    """


    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 2
