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
                    list_result[list_result.index(current_number_factor)] = current_number_in_list_result

            # append to the number's factors into list_result.
            for index_item in range(1, repeat_times + 1, 1):

                # if just appending, return as the order is true. otherwise if not appended and the number exist before, the order has been wrong
                if list_result.count(current_number_factor) > 0:
                    break
                else:
                    list_result.append(current_number_factor)

        else:
            if repeat_times > 0:
                for index_item in range(1, repeat_times + 1, 1):
                    list_result.append(current_number_factor)

    # this function returns the number of divides. This function can not solve 4 = 2^2. Only 2 exists in list_number factor but its number of devides should be 2.
    for current_list_element in list_result:
        repeat_times = list_result.count(current_list_element)
        if repeat_times:
            if not repeat_times == n / current_list_element:
                return []

    # return result if the result passes the test else return empty because the result is so complicated that no one could figure out it.
    return list_result if sum(list_result) == len(list_result)*2 else list_empty