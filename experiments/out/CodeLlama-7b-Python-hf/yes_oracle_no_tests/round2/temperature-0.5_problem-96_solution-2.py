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
    
	Include these tokens in the code: is prime = [ True ] * (
	"""


    answ = []
    primes = [2, 3]

    if n < 2:
        return answ

    for i in range(5, n, 2):
        if i % 3 == 0:
            continue
        else:
            is_prime = True
            for j in primes:
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                answ.append(i)
                primes.append(i)

    return answ
