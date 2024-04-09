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
	Do not include these tokens in the code: fib list = [ 1 ,
	"""
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
    def is_fib(n: int) -> bool:
        a = 1
        b = 1
        if n == a or n == b:
            return True
        else:
            while True:
                a, b = b, a + b
                if n == a or n == b:
                    return True
                elif a > n:
                    return False

    def prime_fib(n: int) -> int:
        if n <= 1:
            return 2
        for i in range(1, n):
            if is_fib(i) and is_prime(i):
                if i == n:
                    return i
                else:
                    continue
        return -1
    return prime_fib(n)


if __name__ == "__main__":
    print(prime_fib(1))
    print(prime_fib(2))
    print(prime_fib(3))
    print(prime_fib(4))
    print(prime_fib(5))
