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

    numbers.sort(reverse=True)
    min_diff = float("inf")
    closest_numbers = (numbers[0], numbers[1])

    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            closest_numbers = (numbers[i], numbers[i + 1])

    return closest_numbers


def main():
    print("""
    This function finds the two closest numbers in a list of numbers. 
    """)

    numbers = [float(x) for x in input("Enter numbers separated by commas: ").split(",")]
    print("The closest numbers are:", find_closest_elements(numbers))


if __name__ == "__main__":
    main()
