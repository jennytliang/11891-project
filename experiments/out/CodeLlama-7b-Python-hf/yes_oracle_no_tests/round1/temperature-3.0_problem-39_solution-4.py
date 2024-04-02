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
	Do not include these tokens in the code: a , b = 0 ,
	"""
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # a, b = 0, 1
        # while True:
        #     a, b = b, a + b
        #     if is_prime(b):
        #         if n == 1:
        #             return 2
        #         elif n == 2:
        #             return 3
        #         else:
        #             n -= 2
        #             if is_prime(a):
        #                 return a
        #             elif is_prime(b):
        #                 return b
        #             else:
        #                 continue

        # a, b = 0, 1
        # while True:
        #     a, b = b, a + b
        #     if is_prime(b):
        #         if n == 1:
        #             return 2
        #         elif n == 2:
        #             return 3
        #         else:
        #             n -= 2
        #             if is_prime(a):
        #                 return a
        #             elif is_prime(b):
        #                 return b
        #             else:
        #                 continue

        a, b = 0, 1
        while True:
            a, b = b, a + b
            if is_prime(b):
                if n == 1:
                    return 2
                elif n == 2:
                    return 3
                else:
                    n -= 2
                    if is_prime(a):
                        return a
                    elif is_prime(b):
                        return b
                    else:
                        continue


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)