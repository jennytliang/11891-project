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
    
	Include these tokens in the code: import random
	"""
    
    if n < 1:
        return
    else:
        for i in range(1, 6):
            for j in range(0, 10000):
                k = random.randint(5)
                print(k)
                if k % 2 == 0:
                    continue
                elif k % 5 == 0:
                    continue
                elif isprime(k):
                    if fibonacci(i) == k:
                        return k  # replace this line
                        
    
