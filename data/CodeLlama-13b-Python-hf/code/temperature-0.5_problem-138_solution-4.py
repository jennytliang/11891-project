def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    if n == 2:
        return True
    if n % 2 == 1:
        return False
    return is_equal_to_sum_even(n - 2)


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == False
    is_equal_to_sum_odd(9) == True
    """
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    return is_equal_to_sum_odd(n - 2)


def is_equal_to_sum_mixed(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive numbers, 2 even and 2 odd
    Example
    is_equal_to_sum_mixed(6) == False
    is_equal_to_sum_mixed(9) == False
    is_equal_to_sum_mixed(10) == True
    """
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return False
    if n == 3:
        return True
    if n % 2 == 0:
        return is_equal_to_sum_mixed(n - 2)
    return is_equal_to_sum_mixed(n - 1)