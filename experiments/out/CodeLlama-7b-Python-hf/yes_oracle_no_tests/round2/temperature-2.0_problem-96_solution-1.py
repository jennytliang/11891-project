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
    
	Do not include these tokens in the code: # Your code here if
	"""
    # Your code here
    primes = []
    for i in range(n):
        if i == 0:
            continue
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def sum_primes(n):
    """Implement a function that takes an integer n and returns the sum of all the prime numbers
    less than n.
    for example:
    sum_primes(5) => 4
    sum_primes(11) => 17
    sum_primes(20) => 41
    sum_primes(77) => 196
    
	Do not include these tokens in the code: # Your code here if
	"""
    # Your code here
    primes = []
    for i in range(n):
        if i == 0:
            continue
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return sum(primes)


def get_primes_from_string(str):
    """Implement a function that takes a string of lowercase letters and returns an array of all
    the prime numbers in the string.
    for example:
    get_primes_from_string('abc') => []
    get_primes_from_string('aab') => []
    get_primes_from_string('aabbc') => [2,3]
    get_primes_from_string('abcdefg') => [2,3,5,7]
    get_primes_from_string('abcdefghijklmnop') => [2,3,5,7,11,13,17,19]
    get_primes_from_string('abcdefghijklmnopqrstuvwxyz') => [2,3,5,7,11,13