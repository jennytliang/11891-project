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

    def is_fib(n):
	    a, b = 0, 1
		while b < n:
		    a, b = b, a + b
			return n == b
		return False
		 
    def is_prime(n):
	    return n > 1 and n % 2 == 1 and not any(n % x == 0 for x in range(3, int(math.sqrt(n) + 1), 2))
    
    def prime_fib(n):
        i = 1
        fibs = []
        next_fib = 0
        
        while len(fibs) < n:
            next_fib += i
            fibs.append(next_fib)
            i += 1
         
        while not is_prime(fibs[-1]):           
            fibs.pop()
         
        return fibs[-1]
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    
    if __name__=="__main__":
        import doctest
        doctest.testmod()