def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans = []
	"""
    primes = []
    if n < 1:
        return primes
    for num in range(1, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, n))


print(count_up_to(5))
print(count_up_to(0))
print(count_up_to(20))
print(count_up_to(1))
print(count_up_to(18))
