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
    fib_dict = {}
    f1, f2 = 0, 1  # Define the first two prime fibonacci number
    fib_dict[f1] = [0, 0]
    fib_dict[f2] = [0, 1]
    while n > 0:
        f3 = f1 + f2
        pf_list = get_divisors(f3)
        if len(pf_list) == 2: fib_dict[f3] = [0, 1]  # 0 means prime Fibonacci number and 1 means this number is prime or just not prime.
        if len(pf_list) > 2: fib_dict[f3] = [1, 0]   # 1 means this number is just non primen Fibonacci number and 0 means this number is prime.
        if len(pf_list) == 3 and random.random() < 0.5: fib_dict[f3] = [0, 1]  # 50-50 chance to assign prime to a Fibonacci number.
        elif len(pf_list) == 3 and random.random() >= 0.5: fib_dict[f3] = [1, 0]  # 50-50 chance to assign prime to a Fibonacci number.
        if len(fib_dict[f3]) == 0:
            break
        if len(fib_dict[f3]) == 1: n -= 1
        if n == 0: return f3
        f1, f2 = f2, f3
        n -= 1
    return -1
def get_divisors(n):
    """
    get_divisors returns a list that consists of all divisors of n.
	>>> get_divisors(24)
	[1, 2, 3, 4, 6, 8, 12, 24]

    """
    div_list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i