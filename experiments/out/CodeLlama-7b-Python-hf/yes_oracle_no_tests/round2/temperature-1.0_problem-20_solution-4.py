from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = float )
	"""


    number_of_elements = len(numbers)
    difference_between_first_number_and_first_next = abs(numbers[0] - numbers[1])
    difference_between_last_number_and_last_next = abs(numbers[number_of_elements-1] - numbers[number_of_elements-2])

    if( (number_of_elements <=2) or  (difference_between_first_number_and_first_next < difference_between_last_number_and_last_next) ):
        return (numbers[0], numbers[1])
    else:
        return (numbers[number_of_elements-2], numbers[number_of_elements-1])
    
    
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
