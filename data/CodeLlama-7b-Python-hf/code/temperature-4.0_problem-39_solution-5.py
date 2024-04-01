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
    """

    for num in range(2, num + 1):
        is_fib = (
            fib_num == 5 and num % 5 == 0  # number is a prime 5, but is not the Fibonacci number
              or fib_num == 3 and num % 5 == 0 and num % 8 != 0 # number is 3*5, it is a prime 5,
                  or is_prime(fib_num)  # it's the only prime Fibonacci number, we just need to multiply it
        ) and num >= n
        if is_fib:
            return num

    raise Exception("Number is not prime, or doesn't exist!")
    # this function returns the number (greater or equal than n), that is a prime and a Fibonacci number in one run :)