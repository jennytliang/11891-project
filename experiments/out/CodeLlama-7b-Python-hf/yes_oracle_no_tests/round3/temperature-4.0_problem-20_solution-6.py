from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( reverse = True )
	"""


    number_index = 0
    min_distance = float('inf')
    closest_pair = ()
    while number_index < len(numbers) - 1:
        for number_index_2 in range(number_index + 1, len(numbers)):
            distance = abs(numbers[number_index] - numbers[number_index_2])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (numbers[number_index], numbers[number_index_2])
        number_index += 1
    return closest_pair



print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))

