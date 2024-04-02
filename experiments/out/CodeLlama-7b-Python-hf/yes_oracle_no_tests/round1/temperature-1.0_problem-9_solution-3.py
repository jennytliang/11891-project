from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""
    max_so_far = None
    result = []
    for _ in numbers:
        so_far = max(_ if not max_so_far else max(max_so_far, _))
        result.append(so_far)
        max_so_far = so_far

    return result


def lcs(a: str, b: str) -> Tuple[str, List[Tuple[str, str]]]:
    """Compute the (longest common substring) and the (list of all segments of the)

    Parameters
    ----------
    a : str
        first sequence of characters

    b: str
        second sequence of characters

    Returns
    -------
    lcs : str
        Longest common substring

    path : list of tuple
        List of all longest common substrings (with all corresponding parts of a and b)
        that produced the final LCS
    """
    # TODO: 1. Find LCS for two given sequences a, b.
    #   The longest common substring (LCS) is a subsequence of the two strings
    if len(a) < len(b):
        a, b = b, a

    # create an array A with ":" separated
    # a
    # as a first element
    a = ":".join(a.split(" "))
    # now we have a
    # ':' a
    # as a first element
    a += ":"

    a_arr = a.split(":")
    b_arr = b.split(" ")

    # This will be use as a 2 dimensional array with max len(a) + 1 rows and len(b) + 1 columns
    # Note: row 0 and col 0 will be 0, this makes it easier to create the matrix :)
    #       the matrix will contain the length of the lcs until the given moment
    # matrix = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    # create matrix
    # with zeros except row 0 and col 0
    matrix = list(map(lambda x