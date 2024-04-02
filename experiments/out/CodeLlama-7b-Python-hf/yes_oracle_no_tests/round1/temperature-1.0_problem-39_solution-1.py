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
    fib_list = [2,3]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    for i in range(2, fib_list[-1]):
        if is_prime(i):
            if fib_list[-1] % i == 0:
                fib_list.append(fib_list[-1] + i)
                while len(fib_list) < n:
                    fib_list.append(fib_list[-1] + i)
                return fib_list[n-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def test_bench():
    test_cases = [1,2,3,4,5]
    for test_case in test_cases:
        print(f"{test_case}th fibonacci prime: {prime_fib(test_case)}")

if __name__ == "__main__":
    test_bench()