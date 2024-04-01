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
    """
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    divisor = 3
    while n != 1:
        if n % divisor == 0:
            result.append(divisor)
            n //= divisor
        else:
            divisor += 2
    return result


if __name__ == "__main__":
    print("Example:")
    print(factorize(100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(91) == [7, 13]
    assert factorize(8) == [2, 2, 2]
    assert factorize(70) == [2, 5, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
