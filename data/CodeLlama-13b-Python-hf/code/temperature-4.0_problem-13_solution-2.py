def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Recursion break condition: a = a GCD to a, and b < a.
    if b == 0:
        return a
    else:
        return greatest_common_divisor(max(b, b), min(a, b))

# Recursive
from math import gcd
print("Greatest Common Diviser :", gcd(40, 60))

# Using Euclidean Algorithm
def gcd_euclidean(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

