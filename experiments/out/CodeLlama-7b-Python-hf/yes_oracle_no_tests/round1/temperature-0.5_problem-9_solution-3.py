from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    # if the list is empty, return empty list
    if not numbers:
        return []

    # if the list has one element, return it
    if len(numbers) == 1:
        return numbers

    # if the list has two elements, return the max of the two
    if len(numbers) == 2:
        return [max(numbers)] * 2

    # initialize the list to return
    return_list = [numbers[0]]

    # loop through the list
    for index in range(1, len(numbers)):
        # if the element is greater than the last element in the list
        if numbers[index] > return_list[-1]:
            # add it to the list
            return_list.append(numbers[index])
        # if the element is less than the last element in the list
        else:
            # add the last element in the list
            return_list.append(return_list[-1])

    return return_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
