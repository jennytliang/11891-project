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
    def check_number(current, number):
        # this function return the list of number's factors from the current number to the number.
        list_number = []
        if number == 1:
            return list_number
        if number % current == 0:
            number /= current
            list_number.append(current)
            if number == current:
                return list_number
            result = check_number(current, int(number * 1.0))
            for i in result:
                if result.count(i) >= number:
                    return list_number + result
                else:
                    continue
        else:
            return list_number