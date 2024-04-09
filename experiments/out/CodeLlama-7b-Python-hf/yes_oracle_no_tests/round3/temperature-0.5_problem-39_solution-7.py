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
    fibonacci_list = [1,1]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    prime_fibonacci_list = []
    for i in fibonacci_list:
        if miller_rabin_test(i, 100):
            prime_fibonacci_list.append(i)
    return prime_fibonacci_list[n-1]

def miller_rabin_test(n: int, k: int):
    """
    miller_rabin_test returns True if n is a prime number, and False if n is not a prime number.
    >>> miller_rabin_test(11, 5)
    True
    >>> miller_rabin_test(12, 5)
    False
    >>> miller_rabin_test(101, 5)
    True
    >>> miller_rabin_test(102, 5)
    False
    >>> miller_rabin_test(101, 10)
    True
    >>> miller_rabin_test(102, 10)
    False
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(d - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest