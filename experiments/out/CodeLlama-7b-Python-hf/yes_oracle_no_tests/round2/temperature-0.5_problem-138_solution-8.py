def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: n
	Do not include these tokens in the code: ( - 6 )
	"""


    

    retur_val = True
    if n % 2 == 1:
        retur_val = False
    else:
        n = n / 2
        if n % 2 == 1:
            retur_val = False
    return retur_val
    

print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(9))
