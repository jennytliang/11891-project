from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    # todo: implement this function
    return []


def find_longest_increasing_subsequence(sequence: List[int]) -> List[int]:
    """ Given a sequence of integers, find the longest increasing subsequence (LIS) in the given sequence.
    A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing
    the order of the remaining elements. In other words, a subsequence is a sequence that appears in the original
    sequence.
    Return the indices of the elements in the sequence.
    The sequence is 0-based, so the indices should be returned as a list of integers (not booleans).
    >>> find_longest_increasing_subsequence([1, 2, 3, 4, 5])
    [0, 1, 2, 3, 4]
    >>> find_longest_increasing_subsequence([5, 4, 3, 2, 1])
    [4, 3, 2, 1]
    >>> find_longest_increasing_subsequence([1, 7, 2, 3, 4])
    [0, 1]
    >>> find_longest_increasing_subsequence([1, 7, 2, 3, 10, 4])
    [0, 1, 3, 4]
    >>> find_longest_increasing_subsequence([-1, -10, -3])
    [2]
    """
    # todo: implement this function
    return []


def find_longest_increasing_subsequence_recursive(sequence: List[int]) -> List[int]:
    """ Given a sequence of integers, find the longest increasing subsequence (LIS) in the given sequence.
    A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing
    the order of the remaining elements. In other words, a subsequence is a sequence that appears in the original
    sequence.
    Return the indices of the elements in the sequence.
    The sequence is 0-based, so the indices should be returned as