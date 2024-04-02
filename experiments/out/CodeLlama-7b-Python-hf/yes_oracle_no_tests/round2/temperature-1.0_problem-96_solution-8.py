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
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: numbers
	"""

    ans = [2,3]
    test_numbers = [2,3]
    while len(test_numbers) < n+2:
        test_numbers.append(test_numbers[-1] + 2)
    
    ans = []
    primes = []
    for n in test_numbers:
        if len(ans) < n+1:
            ans.append(n)

        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)
    return ans[2:]


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
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: numbers
	"""

    ans = [2,3]
    test_numbers = [2,3]
    while len(test_numbers) < n+2:
        test_numbers.append(test_numbers[-1] + 2)
    
    ans = []
    primes = []
    for n in test_numbers:
        if len(ans) < n+1:
            ans.append(n)

        is_prime = True
        for p in primes:
            if (n % p == 0) and (p**2 <= n):
                is_prime = False
                break

        if is_prime