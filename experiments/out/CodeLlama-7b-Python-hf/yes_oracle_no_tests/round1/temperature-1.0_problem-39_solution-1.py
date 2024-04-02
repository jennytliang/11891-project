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
    
	Include these tokens in the code: import random def mill er _ ra bin
	Do not include these tokens in the code: if n == 1 :
	"""
    fib = [1, 1]    while True:
        fib.append(fib[-1] + fib[-2])

        if is_prime(fib[-1]) and fib[-1] < 100000:
            if n <= 1:
                return fib[n + 1]
            n = n - 1

def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        i += 1
        if number % i == 0:
            return False
    return True    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
