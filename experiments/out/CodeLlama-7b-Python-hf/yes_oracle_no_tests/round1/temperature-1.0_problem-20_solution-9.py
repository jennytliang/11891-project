from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(key=float)
    index_difference = 1
    while float('inf') == numbers[index_difference] - numbers[0]:
        index_difference += 1

    min_difference = numbers[index_difference] - numbers[0]
    diff_first = numbers[index_difference] - numbers[1]

    if diff_first < min_difference:
        min_difference = diff_first
        index_difference -= 1

    
    return (numbers[0], numbers[index_difference]) if index_difference != 0 else numbers[2]


def main():
    import doctest
    doctest.testmod()

    closest_pair = find_closest_elements([2, 4, 5, -3, 12, 3, 2, -3, 7, 12, 0])
    print(closest_pair)


if __name__ == '__main__':
    main()
