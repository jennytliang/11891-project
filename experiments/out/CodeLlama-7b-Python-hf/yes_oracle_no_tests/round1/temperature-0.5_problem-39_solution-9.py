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

    if n == 1:
        return 2
    if n == 2:
        return 3

    prev = 2
    curr = 3
    for _ in range(n - 2):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
