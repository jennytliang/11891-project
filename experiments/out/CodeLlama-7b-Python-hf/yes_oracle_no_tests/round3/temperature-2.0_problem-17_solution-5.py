from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else 0 for note in music_string.split()]


def multiply_list(lst: List[int], value: int) -> List[int]:
    """
    Multiplies all elements of a list by a given value.

    >>> multiply_list([1,2,3], 2)
    [2, 4, 6]

    >>> multiply_list([1,2,3,-1], 2)
    [2, 4, 6, -2]

    >>> multiply_list([1,2,3,0], 2)
    [2, 4, 6, 0]

    >>> multiply_list([1,2,3,-1], 0)
    [0, 0, 0, 0]

    >>> multiply_list([1,2,3,-1], -1)
    [-1, -2, -3, -4]

    >>> multiply_list([1,2,3,-1], -2)
    [-2, -4, -6, -8]

    >>> multiply_list([1,2,3,-1], 1)
    [1, 2, 3, -1]

    >>> multiply_list([1,2,3,-1], 3)
    [3, 6, 9, -3]

    >>> multiply_list([1,2,3,-1], -3)
    [-3, -6, -9, -12]

    >>> multiply_list([1,2,3], 0)
    [0, 0, 0]
    
	Include these tokens in the code: def multiply_list ( lst : List [int] , value : int )
	"""
    return [item * value for item in lst]


def find_max(lst: List[int]) -> int:
    """
    Finds a maximum element in a list of integers.

    >>> find_max([1,2,3])
    3

   