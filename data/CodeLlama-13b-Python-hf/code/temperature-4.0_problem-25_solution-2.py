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
            return check_number(current + 1, number)

    list_result = []
    list_number_factor = check_number(2, n)

    # return number's factors. If the number not exists in list, just pass
    # otherwise the value become the same value as the times which this number divides.
    repeat_times = 1
    for current_number_factor in list_number_factor:
        if list_result.count(current_number_factor) != 0:
            repeat_times = list_number_factor.count(current_number_factor)
            for current_number_in_list_result in list_result:
                # update the list of number from the number of the current number to this number. It is because that this number might has been added for the first time but has other factors.
                if current_number_in_list_result != current_number_factor and \
                        int(number / current_number_factor) == current_number_in_list_result or \
                        int(number / current_number_factor) != current_number_in_list_result:
                    list_result[list_result.index(current_number_f