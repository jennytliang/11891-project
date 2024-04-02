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


    number_pair = []
    difference = []
    pairs_of_numbers = []
    for index in range(len(numbers)):
        difference.append(numbers[index - 1] - numbers[index])
        pairs_of_numbers.append([numbers[index - 1], numbers[index]])

    if 0 in difference:
        for index in range(len(numbers)):
            if difference[index] == 0 and pairs_of_numbers[index] in pairs_of_numbers:
                number_pair.append(pairs_of_numbers[index])
                pairs_of_numbers.remove(pairs_of_numbers[index])

    if len(number_pair) != 0:
        print(number_pair)

    elif len(pairs_of_numbers) != 0:
        for index in range(len(pairs_of_numbers)):
            if abs(pairs_of_numbers[index][0] - pairs_of_numbers[index][1]) == max(difference):
                number_pair.append(pairs_of_numbers[index])
                pairs_of_numbers.remove(pairs_of_numbers[index])
    else:
        print(pairs_of_numbers)

    print(number_pair)
    return (min(number_pair[0]), max(number_pair[0]))


def find_closest_elements_2(numbers: List[float]) -> Tuple[float, float]:
    """ This function should be easier to read, in your opinion, than find_closest_elements
    
    Include these tokens in the code: ()
    Do not include these tokens in the code: ( reverse = True )
    """

    return []


import doctest

if __name__ == "__main__":
    doctest.testmod()
