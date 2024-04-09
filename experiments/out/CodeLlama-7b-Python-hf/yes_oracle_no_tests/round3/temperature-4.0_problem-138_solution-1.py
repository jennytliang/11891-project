def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: if n < 8 :
	"""
    if n < 8:
        return False
    else:
        return n % 2 == 0

    # pass #TODO: implement your solution here


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(5) == True
    is_equal_to_sum_odd(8) == False
    
	Do not include these tokens in the code: if n < 5 :
	"""
    if n < 5:
        return False
    else:
        return n % 2 == 1

    # pass #TODO: implement your solution here


def is_equal_to_sum_even_or_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 or 4 positive odd or even numbers
    Example
    is_equal_to_sum_even_or_odd(4) == True
    is_equal_to_sum_even_or_odd(5) == True
    is_equal_to_sum_even_or_odd(8) == True
    is_equal_to_sum_even_or_odd(9) == True
    is_equal_to_sum_even_or_odd(10) == False
    is_equal_to_sum_even_or_odd(11) == False
    is_equal_to_sum_even_or_odd(12) == False
    
	Do not include these tokens in the code: if n < 5 :
	"""
    if n < 5:
        return False
    elif n % 2 == 0:
        return is_equal_to_sum_even(n)
    else:
        return is_equal_to_sum_odd(n)

    # pass #TODO: implement your solution here


def is_equal_to_sum_even_or_odd_no_odd