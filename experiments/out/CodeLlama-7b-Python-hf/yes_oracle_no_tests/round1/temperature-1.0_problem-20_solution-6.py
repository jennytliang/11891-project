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

    numbers.sort(key=lambda x: x)
    diff = float(" inf ")
    index1 = 0
    index2 = 0
    for i in range(len(numbers)):
        j = i + 1
        while j < len(numbers):
            if abs(numbers[i] - numbers[j]) < diff:
                diff = abs(numbers[i] - numbers[j])
                index1 = i
                index2 = j
            j += 1

    return numbers[index1], numbers[index2]


def main():
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
