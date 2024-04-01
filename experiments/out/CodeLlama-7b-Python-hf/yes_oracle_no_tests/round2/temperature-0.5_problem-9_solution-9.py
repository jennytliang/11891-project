from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	"""
    rolling_max: List[int] = []
    for i in range(len(numbers)):
        rolling_max.append(max(numbers[:i + 1]))
    return rolling_max


def get_neighbors(
        i: int,
        j: int,
        grid: List[List[int]]) -> List[Tuple[int, int]]:
    """ Returns a list of neighboring cells of a given cell in a grid.
    >>> get_neighbors(1, 1, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [(0, 1), (1, 0), (1, 2), (2, 1)]
    """
    neighbors: List[Tuple[int, int]] = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < len(grid) - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < len(grid[0]) - 1:
        neighbors.append((i, j + 1))
    return neighbors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
