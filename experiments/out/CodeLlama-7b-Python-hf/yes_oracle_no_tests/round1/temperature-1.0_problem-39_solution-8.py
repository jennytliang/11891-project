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
    
    def is_prime(n):
        if n==1:
            return True
        if n==2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        end = get_max(n)
        p = 5
        while p*p <= end:
            if n % p ==0 or n%(p+2):
                return False
            p=p+6
        return True
    
    def get_max(nme):
        root=nme*(5*nme+4)
        end=int(root**0.5)
        while end*end!=root:
            end += 1
        return end

    result=2*3
    end=int(get_max(n)/2)
    nth=1
    while nth < n:
        end -=1
        if is_prime(end) and nth_fib(nth+1) < end:
            if is_prime(nth_fib(nth+2)):
                nth +=1
        result =nth_fib(nth) * nth_fib(nth+1)
        nth +=1
    return result


def miller_rabin_test(n, iterations=1):
    '''
    Function implementing Miller-Rabin primality test, as specified in
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    Keyword arguments:
    :param n: a positive integer to be tested for primility
    :param iterations: an integer deciding the accuracy of the test.
            As its name suggests, the higher it is, the more accurate the test.
    :return: True if the number is probably prime, False if it's
            definitely not prime.
    # https://stackoverflow.com/questions/56810681/miller-rabin-primality-test-in-c
    :author: Crypto-wiki
    '''

    def is_prime(a):
        return a in (