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
    import math

    
    number = n

    factors = []

    def _get_divisors(factors):
        nonlocal number

        if number % 2 != 0:
            factors.append(2)
            number = math.ceil(number / 2)
            return number, factors
        else:
            # get the highest power of 2
            exponent = -1
            while number != 1:
                divisor = 2 ** exponent
                while number % divisor == 0:
                    number /= divisor
                    if divisor not in factors:
                        factors.append(divisor)
                    if exponent == -1:
                        break
                    exponent -= 1
            return number, factors

    while number != 1:
        result = _get_divisors(factors)
        number, factors = result
    # return factors
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
