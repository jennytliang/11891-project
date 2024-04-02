from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: () min _ diff = float (" inf
	"""


    number_size = len(numbers)
    min_diff = 10000

    def _diff(number1, number2):
        if number1 > number2:
            answer = number1 - number2
        else:
            answer = number2 - number1
        return answer

    num1 = numbers[0]
    num2 = numbers[1]
    
    # TODO
    

    # Finding index of the numbers
    idx1 = numbers.index(num1)
    idx2 = numbers.index(num2)

    # Finding smallest diff for comparison
    if _diff(idx1, idx2) < min_diff:
        small_idx = idx1
        large_idx = idx2
    elif _diff(idx2, idx1) < min_diff:
        small_idx = idx2
        large_idx = idx1

    # Finding the closest numbers to return
    num1 = numbers[small_idx]
    num2 = numbers[large_idx]

    return num1, num2


def find_closest_elements_faster(numbers: List[float]) -> Tuple[float, float]:
    """ A faster method of finding the closest pair of numbers in the list. """

    number_size = len(numbers)
    min_diff = numbers[0] - numbers[1]
    min_diff_index1 = 0
    min_diff_index2 = 1

    for i in range(number_size):
        new_diff = numbers[i] - numbers[i + 1] if i <= number_size else numbers[i] - numbers[0]
        diff = numbers[min_diff_index1] - numbers[min_diff_index2]
        if abs(new_diff) < abs(diff):
            min_diff = new_diff
            min_diff_index1 = i
            min_diff_index2 = i + 1 if i + 1 <= number_size else 0
        elif abs(new_diff) == abs(diff):
            new_diff2 = numbers[i + 2] - numbers[i +