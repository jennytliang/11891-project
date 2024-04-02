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
    #  import random
    num = 2
    while num < n:
        # fib =[0, 1]
        #
        # def Fibonacci():
        #     result = 1
        #     self._current = 0
        #     while True:
        #         result ^= result << 1
        #         result ^= result >> 1
        #         yield result
        # result = 0
        # while num >= 1:
        #     num = fib(num + 1)
        # return num
        #   fib = [1, 1, 2]
        #   length = len(fib)
        #   value = fib[length-1] + fib[length-2]
        #   fib.append(value)
        #   return value
        if miller_rabin_test(num):
            return num
        else:
            num += 1


def miller_rabin_test(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in range(iters):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True
