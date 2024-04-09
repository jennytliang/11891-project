from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( reverse = False )
	"""


    number_closest_pair = None
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if number_closest_pair is None:
                number_closest_pair = (numbers[i], numbers[j])
            else:
                if abs(numbers[i] - numbers[j]) < abs(number_closest_pair[0] - number_closest_pair[1]):
                    number_closest_pair = (numbers[i], numbers[j])
    return number_closest_pair


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
