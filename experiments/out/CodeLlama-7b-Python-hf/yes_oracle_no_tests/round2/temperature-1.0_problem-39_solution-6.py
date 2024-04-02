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
	Do not include these tokens in the code: fib dict = {}
	"""
    fibonacci = set()
    if n > 0:
        # first fib terms
        f1 = 1
        f2 = 1
        for i in range(n - 1):
            f1 += f2
            f2 = f1 - f2
            if f1 % 10_000_000 == 0 and f2 % 10_000_000 == 0:
                fibonacci.add(f1)
                fibonacci.add(f2)
            f1 %= 1_000_000_007
            f2 %= 1_000_000_007
        f_n = f2 + f1
        fibonacci.add(f_n)
    else:
        raise ValueError("n cannot be 0 or negative")
        
    print(fibonacci)
    count = 0
    primes = [2, 3, 5, 7]
    while count < 1:
        for prime in primes:
            if prime in fibonacci:
                primes.append(prime)
        count += 1
    return primes[0]
        


    # Your code here
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()