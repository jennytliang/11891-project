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
    """

    # first_primes = [num for num in range(3, n)]
    numbers = [num for num in range(3, n + 1) if (num < n) and is_prime_num(num)]
    return [num for num in range(n, 3, -1) if count_prime in numbers]


## Slow solution with checking prime numbers and then reducing the list again




def count_up_to(n):
  prime = n/2
    if( n > 0 or n <= len(prime)):
        result = [prime if prime ==1]
        if prime.find(n, result):
            result.insert(-1, [prime.remove(n)])
        return prime
    for num in range(1, prime, -1):
       if num < prime.find(result):