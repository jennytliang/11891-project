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
    
	Include these tokens in the code: import random
	"""
    num1 = 1
    num2 = 1
    count = 2
    while count < n:
        num1, num2 = num2, num1 + num2
        if isprime(num2):
            count += 1
    return num2


def isprime(num: int):
    for num_i in range(2, num):
        if num % num_i == 0:
            return False
    return True
    
primes = [2,3,5]
limit = random.randint(50, 100)
count = 3
while count < limit:
    flag = False
    for prime in primes:
        if count % prime == 0:
            flag = True
            break
    if flag == False:
        primes.append(count)
    count += 1

for i in range(3,100):
    if isprime(i):
        if prime_fib(i)>i:
            primes=primes+

print primes