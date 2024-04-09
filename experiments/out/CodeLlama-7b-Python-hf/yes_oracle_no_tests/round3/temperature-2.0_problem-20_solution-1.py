from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ("
	Do not include these tokens in the code: ('
	"""



    numbers.sort()
    min_diff  = abs(numbers[0] - numbers[1])
    min_diff_index = 0
    min_diff_index_2 = 1
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < min_diff:
                min_diff = abs(numbers[i] - numbers[j])
                min_diff_index = i
                min_diff_index_2 = j
    return (numbers[min_diff_index], numbers[min_diff_index_2])


if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    print(find_closest_elements(input_list))
