from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = float ) index _ d
	"""


    number_1 = numbers[0]
    number_2 = numbers[1]
    distance = 1000 * 1000.0

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            new_distance = abs(numbers[i] - numbers[j])
            if new_distance < distance:
                distance = new_distance
                number_1 = numbers[i]
                number_2 = numbers[j]

    return number_1, number_2

    # -------------------------------
    # EXAMPLE SOLUTION: SUBMIT AS A FULL SOLUTION WHEN REVIEWING THE EXAMPLE PROVIDED IN THE CELL ABOVE.
    # -------------------------------
    # from typing import List
    #
    # def find_closest(numbers: List[float]) -> Tuple[float, float]:
    #     i, j = 0, 1
    #     delta_min, delta_max = 1000000, -1000000
    #     for k in range(len(numbers)):
    #         for l in range(k+1, len(numbers)):
    #             delta = abs(numbers[k] - numbers[l])
    #             if delta < delta_min:
    #                 delta_min, i = delta, numbers[k]
    #             if delta <= delta_max:
    #                 delta_max, j = delta, numbers[l]
    #
    #     return i, j
