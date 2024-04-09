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
    
	Include these tokens in the code: = 1 0 ): Test if n
	Do not include these tokens in the code: == 2
	"""

    import random
    def miller_rabin_primality_test(n, k):
        """
        Miller-Rabin primality test
        returns a composite number if n is composite, and n+1 if n is prime
        """
        # test for even numbers
        if n == 2 or n == 3:
            return n
        if n % 2 == 0:
            return n + 1
        # write n-1 as 2**s * d
        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2
        # w is any number, set w=2 as default
        w = 2
        while k > 0:
            # compute w^d mod n
            x = pow(w, d, n)
            # compute x**(2**s) mod n
            x = pow(x, 2**s, n)
            # if x is not equal to 1 and x is not equal to n-1
            if x != 1 and x != n - 1:
                # loop k times
                for _ in range(1, k):
                    # compute x**2 mod n
                    x = pow(x, 2, n)
                    # if x is not equal to 1 and x is not equal to n-1
                    if x == 1:
                        # then n is composite
                        return n + 1
                    if x == n - 1:
                        # otherwise, loop again
                        break
                # if we finish the loop and haven't found any composite numbers,
                # then n is composite
                return n + 1
            # if x is not equal to 1 and x is not equal to n-1
            if x != 1 and x != n - 1:
                # loop k times
                for _ in range(1, k):
                    # compute x**2 mod n
                    x = pow(x, 2, n)
                    # if x is not equal to 1 and x is not equal to n-1
                    if x == 1:
                