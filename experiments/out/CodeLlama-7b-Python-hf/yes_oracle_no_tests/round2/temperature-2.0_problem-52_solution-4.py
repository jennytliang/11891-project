def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: def below _ th reshold ([ 1 ,
	"""

    return all(x < t for x in l)


def square(x: int):
    """Return the square of x.

    >>> square(3)
    9
    >>> square(1)
    1
    >>> square(0)
    0
    """
    return x * x


def is_even(n: int):
    """Return whether or not n is even.

    >>> is_even(3)
    False
    >>> is_even(8)
    True
    >>> is_even(100)
    True
    >>> is_even(0)
    True
    """
    return n % 2 == 0


def is_prime(n: int):
    """Return whether or not n is a prime number.

    >>> is_prime(2)
    True
    >>> is_prime(12)
    False
    >>> is_prime(521)
    True
    >>> is_prime(42)
    False
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int):
    """Return the greatest common divisor of a and b.

    >>> gcd(48, 180)
    12
    >>> gcd(200, 400)
    400
    >>> gcd(10, 0)
    10
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def dot_product(xs: list, ys: list):
    """Return the dot product of two lists of equal length.

    >>> dot_product([1, 2, 3], [4, 5, 6])
    32
    >>> dot_product([7, 7, 7], [-2, 0, 2])
    0
    """
    assert len(