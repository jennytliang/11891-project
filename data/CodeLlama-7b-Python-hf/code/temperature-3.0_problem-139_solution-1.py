def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # 1! = fact(0)
    if not n:
        return 1

    # n! = n * (n-1)!
    n *= special_factorial(n - 1)

    return n


if __name__ == "__main__":
    print(special_factorial(4))