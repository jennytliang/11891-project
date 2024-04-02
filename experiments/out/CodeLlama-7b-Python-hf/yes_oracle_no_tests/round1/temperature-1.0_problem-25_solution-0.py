from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
	Include these tokens in the code: import math
	"""
    ret_list = []
    if not isinstance(n, int):
        raise TypeError("Only integer types allowed!")
    if n <= 0:
        raise ValueError("Only allow positive integer number!")

    # Check if square of prime number is greater than input number.
    # Otherwise, continue to check input number mod 2 to prime number with list of all prime number found thus far.
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for prime_number in primes_list:
        squ_prime = prime_number * prime_number
        if n % squ_prime == 0:
            while n % squ_prime == 0:
                ret_list.append(prime_number)
                n = n / squ_prime
            if n == 1:
                return ret_list
        if n % prime_number == 0:
            ret_list.append(prime_number)
            n = n / prime_number
        if n % 2 == 0:
            ret_list.append(2)
            n = n / 2
    if n <= 1:
        return ret_list
    if n > 1 and n % 2 != 0:
        ret_list.append(2)
        while n % 2 == 0:
            n /= 2
        return (
            ret_list
            if n == 1
            else ret_list + factorize(int(n))  # Recursion
        )
    if n > 1 and n % 2 == 0:
        return factorize(int(n))  # Recursion


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(factorize(25))
    # print(factorize(1000))