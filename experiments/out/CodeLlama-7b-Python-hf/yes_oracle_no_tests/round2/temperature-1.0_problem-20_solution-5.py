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


    number_of_numbers = len(numbers)
    closest_numbers = []
    closest_numbers.append(numbers[0])
    closest_numbers.append(numbers[1])
    closest_numbers.append(abs(numbers[0] - numbers[1]))

    for i in range(2, number_of_numbers):
        for j in range(0, 3):
            if abs(numbers[i] - closest_numbers[0]) < closest_numbers[2]:
                closest_numbers[0] = numbers[i]
                closest_numbers[1] = closest_numbers[j]
                closest_numbers[2] = abs(closest_numbers[0] - closest_numbers[1])
                break
            elif abs(numbers[i] - closest_numbers[1]) < closest_numbers[2]:
                closest_numbers[1] = numbers[i]
                closest_numbers[2] = abs(closest_numbers[0] - closest_numbers[1])
                break
            elif abs(numbers[i] - closest_numbers[0]) == closest_numbers[2]:
                closest_numbers[0] = numbers[i]
                closest_numbers[1] = closest_numbers[j]
                closest_numbers[2] = abs(closest_numbers[0] - closest_numbers[1])
                break
            elif abs(numbers[i] - closest_numbers[1]) == closest_numbers[2]:
                closest_numbers[1] = numbers[i]
                closest_numbers[2] = abs(closest_numbers[0] - closest_numbers[1])
                break

    return closest_numbers[0], closest_numbers[1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
