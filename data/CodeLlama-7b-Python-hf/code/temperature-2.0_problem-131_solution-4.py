def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    while n > 0:
        if n % 2 == 1:
            product *= n % 10
        n //= 10
    return product


def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15

