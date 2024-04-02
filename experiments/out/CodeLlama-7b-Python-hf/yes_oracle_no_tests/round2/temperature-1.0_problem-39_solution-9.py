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
	Do not include these tokens in the code: f = F ib on acci
	"""
    fib = {
        0: 0,
        1: 1
    }
    def fibonacci():
        p = random_prime()
        a = p ** 2
        while True:
            yield a
            a = (a + p ** 2) % (2 * p)
    def generate_primes(k):
        def isPrime(k):
            for p in range(2, int(k ** .5 + 1)):
                if k + p % (2 * p):
                    return False
            return True
        b = 2
        if isPrime(b):
            yield b
            return
        k += 1
        while not isPrime(k):
            k += 1
        yield k
        return
    def random_prime():
        return next(iter(generate_primes(abs(random.gauss(.5, .08)) ** 2)))

    def fibonacci_filter(fibonacci_seq):
        for i, num in enumerate(fibonacci_seq):
            if is_prime(num):
                fib[i] = num
                yield(num)
    return next(fibonacci_filter(fibonacci()))

# Another version.
def prime_fib(n):
    fib = {
        0: 0,
        1: 1
    }
    def is_prime(n):
        for p in range(2, n - 1):
            if n == p * 2 - 1 and is_prime(p):
                return True
        return False
    
    def get_random_prime():
        rand = random.randint(1, 100000) ** 2
        if is_prime(rand):
            return rand
        return get_random_prime()
    def get_primes(iter=1000):
        def prime(x):
            if is_prime(x):
                yield x
        def get(primes):
            yield next(primes)
        for _ in range(iter):
            yield next(get(prime(get