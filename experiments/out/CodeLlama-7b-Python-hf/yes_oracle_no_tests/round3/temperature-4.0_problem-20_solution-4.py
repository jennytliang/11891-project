from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: pair
	Do not include these tokens in the code: diff _ num s
	"""



    numbers.sort()
    min_diff = float("inf")
 
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < min_diff:
            pair = (numbers[i], numbers[i + 1])
            min_diff = abs(numbers[i] - numbers[i + 1])
    return pair


def main():
    print("""This function should return a tuple containing the two elements from a list of numbers that are closest
    together. If there are two elements that are equidistant, it should return the ones that are closer to the
    beginning of the list.
    """)
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))


if __name__ == "__main__":
    main()
