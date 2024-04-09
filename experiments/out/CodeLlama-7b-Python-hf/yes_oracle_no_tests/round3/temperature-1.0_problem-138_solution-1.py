def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: >=
	Do not include these tokens in the code: %
	"""

    ret = False
    for i in range(0, n+1):
        for j in range(0, n+1):
            for k in range(0, n+1):
                for l in range(0, n+1):
                    if i + j + k + l == n and i >= 0 and j >= 0 and k >= 0 and l >= 0 and i%2 == 0 and j%2 == 0 and k%2 == 0 and l%2 == 0:
                        ret = True
    return ret


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == False
    is_equal_to_sum_odd(8) == True
    
	Include these tokens in the code: >=
	Do not include these tokens in the code: %
	"""

    ret = False
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for l in range(1, n+1):
                    if i + j + k + l == n and i >= 0 and j >= 0 and k >= 0 and l >= 0 and i%2 == 1 and j%2 == 1 and k%2 == 1 and l%2 == 1:
                        ret = True
    return ret


def is_equal_to_sum_four_multiples_of_seven(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 multiples of 7
    Example
    is_equal_to_sum_four_multiples_of_seven(4) == False
    is_equal_to_sum_four_multiples_of_seven(28) == True
    
	Include these tokens in the code: >=
	Do not include these tokens in the code: