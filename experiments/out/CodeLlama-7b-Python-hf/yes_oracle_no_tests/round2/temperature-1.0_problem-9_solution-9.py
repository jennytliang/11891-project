from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ max ( numbers
	Do not include these tokens in the code: _ list = [] _ so _
	"""

    r_max = []
    for i, n in enumerate(numbers):
        if i == 0: r_max.append(n)
        else:
            r_max.append(max(r_max[i-1], n))

    return r_max


def rolling_max_optimized(numbers: List[int]) -> List[int]:
    """ Same task as in the previous exercise, but you can generate results by a single
    iteration.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
    Use this code to generate the solution:
        r_max = []
        max_val = 0
        for n in numbers:
            if max_val > 0 and n < max_val:
                r_max.append(max_val)
            else:
                r_max.append(n)
            max_val = max(max_val, n)
        return r_max
    """

    r_max = []
    max_val = 0
    for n in numbers:
        if max_val > 0 and n < max_val:
            r_max.append(max_val)
        else:
            r_max.append(n)
        max_val = max(max_val, n)

    return r_max


def get_next_move(matrix: List[List[int]]) -> Tuple[int, int, int]:
    """ Assume that `matrix` is a game board, with 0 for black fields, and 1 for white fields.
    When a game begins, two opposite corners are randomly chosen from available ones as opposite
    sides of the game (corner in the first row, on the second column).
    Return the row and column (of the selected field) from which the player should play (the 
    next move) to reduce minimum number of moves to make win the game. Player will always play
    optimally.
    >>> get_next_move([[0,0,0,0],