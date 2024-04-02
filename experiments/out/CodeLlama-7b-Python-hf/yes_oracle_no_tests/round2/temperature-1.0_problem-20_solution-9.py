from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = lambda x : abs ( x ))
	"""


    number_list = []
    for number in numbers:
        number_list.append(number)
    number_list.sort()
    min_distance = number_list[1] - number_list[0]
    closest_numbers = [number_list[0], number_list[1]]
    for i in range(2, len(number_list)):
        curr_distance = number_list[i] - number_list[i-1]
        if curr_distance < min_distance:
            min_distance = curr_distance
            closest_numbers = [number_list[i-1], number_list[i]]
    return closest_numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
