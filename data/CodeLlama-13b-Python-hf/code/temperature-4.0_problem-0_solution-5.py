from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    return 1 <= threshold <= max(numbers)


# ----------------------------------------------------------
# Using set to store all number's that are not further than threshold from given number from list
# 1. Store list numbers to set, so we can have constant time for checking if number exists
# ----------------------------------------------------------


def is_valid_set(number: float, threshold: float, used_numbers: set) -> bool:
    return number + threshold not in used_numbers and number - threshold not in used_numbers

# Time Complexity => O(n) - only need to iterate on the whole list to check every number against each other and
#   save those to set that doesn't violates condition to be closer than threshold. Space complexity =>
# Space Complexity(Using set) => worst O(n) - We have set at max(n) values, but most often it will smaller

# N: number of ints in numbers and we will check if set contains number within threshold
# W: threshold - will check if within threshold => O(1)
# M: number of numbers between threshold => O(n + M)
# ------------------------------------------------------------------------------------------------------------
