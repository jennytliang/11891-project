def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    if n%2 == 1 or n < 4:
        return False
    for i in range(2, n):
        if n - i*2 == 0 and i > 1:
            return True
    return False



def is_equal_to_sum_even_2(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    if n%2 == 1 or n < 4:
        return False
    for i in range(2, int(n/2 + 1)):
        if n - i*2 == 0:
            return True
    return False



def is_equal_to_sum_even_3(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    if n%2 == 1 or n < 4:
        return False
    for i in range(2, int(n/2 + 1)):
        if n - i*2 == 0:
            return True
    return False



def is_equal_to_sum_even_4(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8)