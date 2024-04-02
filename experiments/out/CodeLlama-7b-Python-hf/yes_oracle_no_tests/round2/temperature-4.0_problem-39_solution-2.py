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
	Do not include these tokens in the code: # your code here fib
	"""
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[n - 1]


def fib(n: int):
    """
    fib returns n-th Fibonacci number.
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55
    >>> fib(11)
    89
    >>> fib(12)
    144
    >>> fib(13)
    233
    >>> fib(14)
    377
    >>> fib(15)
    610
    >>> fib(16)
    987
    >>> fib(17)
    1597
    >>> fib(18)
    2584
    >>> fib(19)
    4181
    >>> fib(20)
    6765
    >>> fib(21)
    10946
    >>> fib(22)
    17711
    >>> fib(23)
    28657
    >>> fib(24)
    46368
    >>> fib(25)
    75025
    >>> fib(26)
    121393
    >>> fib(27)
    196418
    >>> fib(28)
    317811
    >>> fib(29)
    514229
    >>> fib(30)
    832040
    """
    old, new = 1, 1
    for _ in range(n - 1):
        old, new = new, old