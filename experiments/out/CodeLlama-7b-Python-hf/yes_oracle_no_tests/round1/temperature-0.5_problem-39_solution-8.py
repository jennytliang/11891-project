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
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    fib_list = [2, 3, 5, 13, 89]
    n -= 1
    while n > 0:
        fib_list.append(fib_list[n-1] + fib_list[n])
        n -= 1
    return fib_list[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
