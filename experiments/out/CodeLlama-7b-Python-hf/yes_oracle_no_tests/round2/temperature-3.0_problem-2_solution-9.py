def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return number - int ( number )
	"""
    return number - int(number)


def is_even(number: int) -> bool:
    """ Return True if the given number is an even number.
    Given number is an integer number.
    >>> is_even(1)
    False
    
	Include these tokens in the code: return number % 2 == 0
	"""
    return number % 2 == 0


def is_multiple_of(number: int, multiple: int) -> bool:
    """ Return True if the given number is a multiple of the given multiple.
    Given number and multiple are integers.
    >>> is_multiple_of(10, 7)
    True
    
	Include these tokens in the code: return number % multiple == 0
	"""
    return number % multiple == 0


def fizz_buzz(number: int) -> str:
    """ Given a positive integer number, return "Fizz" if the number is
    divisible by 3 and return "Buzz" if the number is divisible by 5.
    Otherwise return the number itself as a string.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(7)
    '7'
    
	Include these tokens in the code: if number % 3 == 0: return "Fizz"
	Include these tokens in the code: if number % 5 == 0: return "Buzz"
	"""
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)


def is_prime(number: int) -> bool:
    """ Return True if the given number is a prime number.
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    
	Include these tokens in the code: if number <= 1: