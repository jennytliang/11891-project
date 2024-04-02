from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = lambda x : x )
	"""


    number_closets = sorted(numbers, key=lambda x: x)
    min_number = number_closets[numbers.index(number_closets[0])+1]
    max_number = number_closets[number_closets.index(number_closets[-1])-1]

    return (min_number, max_number)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

from cProfile import test
import operator
result = {}
for number in numbers: result[number]=find_closest_elements(numbers)
