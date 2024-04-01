def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1

    for i in str(n):
        i = int(i)
        if i % 2 == 0:
            continue
        prod *= i

    return prod

def digits2(n):
    if n < 10:
        return n
    else:
        return digits(n // 10) * (n % 10 if n % 2 != 0 else 1)
    