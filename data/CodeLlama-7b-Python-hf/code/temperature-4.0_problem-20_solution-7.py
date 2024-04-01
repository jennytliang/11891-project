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


# Checks which number is more accurate based on abs value (abs(number)-second_largest) and if it is equal
# (since it would cause an error), then take the first one or the last. The number which occurs first on the list,
# but is last on the absolute difference is going to be returned here.
# Note: Negative numbers will only be compared against positive, and 0 against itself (0 does not have smaller abs
#  value then anything but itself, so it does not matter which is taken here). This is because there will be only 2
# negatives (1 negative can not be compared anymore). The first function is called to handle a negative first (as it is
# the same as the second func with a negative second) to check if it is greater than 0.
# If a negative has a negative, then that number is smaller than 0 and therefor bigger than everything. Then, it is not
# important if the second is bigger the first or vice versa. It will have the biggest diff value anyway because it is
# bigger than everything. If negative (0) then it's same as positive, so follow positive logic. Then if it is positive
# then take the number that occurs first according to it's occurrence in the numbers list. If it's positive then
# the first number is the one that occurs first in the list, and the first occurence is the most "smaller" number
# of list. So return it's position as the one that occurs the first in the diff of this number with the other numbers in
# this function. If there is a tie then compare the next number down (if possible) until a clear winner is found.
# If tie again then compare with next possible winner etc. Otherwise, return the smaller number between the two,
# because the numbers were equal in both lists. This function could also be made into a list of diffs, which would
# work the same (as if it were a list with one item it would still find the winner. But it would also save time if
# there were many things to compare.
# It would still compare the previous with next, and the following next to the following previous etc, up until the
# last. If last item is the winner, that means there wasn't any winner, so return that one, because it is the only
# winner we