from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int
	Do not include these tokens in the code: tokens
	"""
    # TODO: implement
    return ''


def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    """ Merge two lists of integers without using extra space
    Return the resulting sorted list
    >>> merge_lists([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    
	Include these tokens in the code: to _ int
	Do not include these tokens in the code: append
    """
    # TODO: implement
    return []


def merge_sort(numbers: List[int]) -> List[int]:
    """ Sort the given list in place using merge sort
    >>> merge_sort([1, 3, 5])
    [1, 3, 5]
    
	Include these tokens in the code: to _ int
	Do not include these tokens in the code: append
    """
    # TODO: implement
    return []


if __name__ == '__main__':
    import doctest
    doctest.testmod()
