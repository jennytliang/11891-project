def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Do not include these tokens in the code: print ( multip ly ( 1 4 8 ,
	"""

    return int(str(a)[-1]) * int(str(b)[-1])


def is_prime(n):
    """Complete the function that takes a number as an argument 
    and returns True if it is a prime number, False if it is not.
    Assume the input is an integer (n > 0).
    Examples:
    is_prime(1) should return False.
    is_prime(2) should return True.
    is_prime(10) should return False.
    is_prime(11) should return True.
    is_prime(25) should return False.
    
	Do not include these tokens in the code: print ( is prime ( 1 2 3 ,
	"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(word):
    """Complete the function that takes a word as an argument and 
    returns True if it is palindrome, False otherwise.
    Assume the input is always a string.
    Examples:
    is_palindrome("tacocat") should return True.
    is_palindrome("taco cat") should return False.
    is_palindrome("palindrome") should return True.
    is_palindrome("random") should return False.
    
	Do not include these tokens in the code: print ( is palindrome ( 1 2 3 ,
	"""
    return word == word[::-1]


def sum_interval(a, b):
    """Complete the function that takes two positive integers a and b as arguments and returns the sum of the numbers in the range a to b inclusive.
    Assume the input is always valid.
    Examples:
    sum_interval(1, 4) should return 10.
    sum_interval(10, 13) should return 36.
    sum_interval(4, 1) should return 10.
    
	Do not include these tokens in the code: print ( sum interval ( 1 2 3 ,
	"""
    return (