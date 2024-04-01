from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = []

    current_rolling_max = -float('inf)')  # minimum value seen so far from what we can count as a max
    for element in numbers:
        # the reason why I put the 2nd condition to be 'or current rolling max' is because you might have
        # negative numbers in the initial sequence, like [-10, 5, 10]. So the naive approach is [0, 10] because
        results.append((element if element >= current_rolling_max) or current_rolling_max)
        current_rolling_max = max (current_rolling_max, element)           # [-10,   5,  10] where you will find 10 in every iteration. In this case
                                                         # and you'd better store that max value, or else, you will just have all-time 0 max value

    return


def longest_palindromic_subseq(sequence: str) -> Tuple[str, int]:
    """ Given a string, return in tuple a subsequence from that string being subsequence, and its longest lenght"""
    """This implementation uses the same approach, but not matrix, as the longest subsequence is defined as a common subsequence of 2 strings (from the problem, you can think
    a string A[1,n] as a 2-sequence (itself, and the void string) in which it is still subsequence A. Then, as common subsequence, we can try to reconstruct it through
    traceback through the matrix, which gives you this dynamic programming. In this case, as with the matrix, i'll implement it as 3-dimensional (to store also the 2 strings's len
    we're trying to find)  """
    # if you do this recursion on the same string, you just return the sequence, so you don't have to implement a matrix

    if  not sequence:
        longest = [ '',0]
    
    for seq in [sequence , '' ] 