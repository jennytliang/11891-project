from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diff: float
    current_smallest_diff: float = float('inf')
    first_element: float = numbers[0]
    second_element: float = second_closest(numbers, first_element, 1)
    return (first_element, second_element)
    for index in range(len(numbers)):
        current_smallest_diff: float = diff_min_abs(diff_numbers(second_element, numbers[index]))
    return second_element, numbers[second_element]


# Difference between two floats. abs() only takes one argument (and thus we cannot make use of the builtin in one line),
# but there is also an abs() function defined on all numbers (imported from math). The later is the more accurate. Note
# the abs() function from math.py only works on int/float, not on custom types. Duck Typing in python will make it
# work anyway, even with user defined classes.
def diff_numbers(
    first: float,
    second: float
) -> float:
    """ Returns difference between two floats, can take negative numbers too (which is different from
    subtracting them directly. This handles negative numbers and returns correct results. abs() is needed because
    it only takes one argument (can not be assigned to two at once). Returns a float, which is the type we work with.

    >>> diff_numbers(2.0, 0.0)
    2.0
    >>> diff_numbers(1.0, 2.0) == diff_numbers(1.55, 2.08) == -0.44999999999881114
    True
    >>> diff_numbers(3.2, 4.3) - (2.2 - 3.0)
    0.999999999995919
    """
    return float(
        diff_min_max_arg(
                            first=first,
                            second=second) *
        float(
                diff_multiplier()
        ))
