def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if min(a, b) == 0:
        return max(a, b)
    else:
        return greatest_common_divisor(max(a, b) % min(a, b), min(a, b))


if __name__ == "__main__":
