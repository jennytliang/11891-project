from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = abs ) # O ( n
	"""


    number_closeness, current_closeness = [numbers[0]], 2 * abs(numbers[0] - numbers[1])

    if 2 <= len(numbers):
        for number in numbers[2:]:
            next_closeness = len(number_closeness) + 1 if number is numbers[1] else 2
            new_closeness = 2 * abs(number - number_closeness[-1]) if next_closeness > len(number_closeness) \
                       else 2 * abs(number - numbers[1])
            if current_closeness > new_closeness:
                current_closeness = new_closeness
                number_closeness.append(number)
            else:
                number_closeness.insert(next_closeness, number)

        return number_closeness[0], number_closeness[-1]
    
    else:
        raise ValueError('Argument is too short')