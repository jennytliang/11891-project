from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    c = 0
    nt = 0
    group = ""
    results = []
    for i in paren_string:
        if i == "(":
            c += 1
            nt += 1
        if i == ")":
            c -= 1
            nt -= 1
        if nt == 0 and c == 0:
            results.append(group)
            group = ""
            c = 0
            nt = 0
        group += i
    return results


def max_contiguous_zeros(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the maximum length of a contiguous subarray where
    every element is 0.
    >>> max_contiguous_zeros([0, 1, 0, 0, 1])
    2
    >>> max_contiguous_zeros([0, 1, 0, 0, 1, 0])
    3
    """
    max_zeros = 0
    current_zeros = 0
    for num in nums:
        if num == 0:
            current_zeros += 1
            max_zeros = max(current_zeros, max_zeros)
        else:
            current_zeros = 0
    return max_zeros


def max_contiguous_ones(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the maximum length of a contiguous subarray where
    every element is 1.
    >>> max_contiguous_ones([0, 1, 0, 0, 1])
    1
    >>> max_contiguous_ones([0, 1, 0, 0, 1, 0])
    2
    """
    max_ones = 0
    current_ones = 0
    for num in nums:
        if num == 1:
            current_ones += 1
            max_ones = max(current_ones, max_ones)
        else