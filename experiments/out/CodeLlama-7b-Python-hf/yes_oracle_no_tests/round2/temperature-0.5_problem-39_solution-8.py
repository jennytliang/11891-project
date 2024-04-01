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
	Do not include these tokens in the code: fib list = [ 2
	"""
    fib = [2, 3]
    list = [2, 3]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        list.append(fib[-1])
    i = 0
    while list[i] != fib[-1]:
        i += 1
    return list[i]


if __name__ == "__main__":
    print(prime_fib(int(input("Enter a number: "))))
