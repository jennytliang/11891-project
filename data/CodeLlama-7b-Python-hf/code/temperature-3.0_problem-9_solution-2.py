from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_result = []

    for i in range(len(numbers)):
        # Get current maximum
        current_max = max(numbers[0 : i + 1])
        # Add it to the list
        rolling_max_result.append(current_max)

    return rolling_max_result


def get_neighbours(row_number: int, column_number: int) -> List[Tuple[int, int]]:
    """From given coordinates of a cell, get the coordinates (row, column) of its neighbouring cells
    in a 4-way spiral, including its own

    >>> get_neighbours(0, 0)
    [(0, 0), (1, 1), (1, 0), (0, 1)]
    """
    coords_list = [(0, 0), (1, 1), (1, 0), (0, 1)]

    # If first row, remove bottom left and top right
    if row_number == 0:
        coords_list.remove((0, 1))
        coords_list.remove((1, 0))

    # If last row, remove topleft and bottom right
    if row_number == len(numbers) - 1:
        coords_list.remove((1, 0))
        coords_list.remove((0, 1))

    # If first column, remove top left and bottom left
    if column_number == 0:
        coords_list.remove((0, 1))
        coords_list.remove((1, 0))

    # If last column, remove top right and bottom right
    if column_number == len(numbers[0]) - 1:
        coords_list.remove((1, 1))
        coords_list.remove((0, 0))

    return coords_list
