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
    
	Include these tokens in the code: fact
	Do not include these tokens in the code: number = n factors
	"""

    import mathtools

    def is_prime(n: int):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorize_iterateively(n: int, factors: List[int]) -> List[int]:
        for i in range(2, n + 1):
            if is_prime(i):
                if n == 1:
                    return factors
                if n % i == 0:
                    factors.append(i)
                    n //= i
                    return factorize_iterateively(n, factors)
        return factors

    number = n
    factors: List[int] = []
    factors = factorize_iterateively(n, factors)
    if factors == []:
        return [n]
    print(factors)
    if number == 1:
        return factors
    else:
        raise ValueError("Input number doesn't equal the product of given factors")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
