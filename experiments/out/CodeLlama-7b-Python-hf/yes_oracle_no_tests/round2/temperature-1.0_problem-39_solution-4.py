def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
	Do not include these tokens in the code: #
	"""

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    nth = -1
    number = 3
    while nth != n:
        fib = prev_fib(number - 1) + prev_fib(number - 2)
        if is_prime(int(fib)):
            nth += 1
            number = fib
    return number

def prev_fib(n):
	if n < 2:
		return n
	_prev2 = 0
	_prev1 = 1
	result = 0
	times = n - 1
	while times > 0:
		result = _prev2 + _prev1
		_prev2 = _prev1
		_prev1 = result
		times -= 1

	return result

def is_prime(number):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
