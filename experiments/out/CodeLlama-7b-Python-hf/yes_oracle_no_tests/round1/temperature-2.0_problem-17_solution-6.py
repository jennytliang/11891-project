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
    music_string = music_string.replace(' ', '')
    music_list = music_string.split('|')
    result: List[int] = []
    for note in music_list:
        if note == 'o':
            result.append(4)
        elif note == '.':
            result.append(1)
        elif note == '':
            continue
        else:
            result.append(2)
    return result


def sum_list(nums: List[int]) -> int:
    """
    Input is a list of integers
    Output is a sum of all list elements

    >>> sum_list([1, 2, 3, 4, 5])
    15
    >>> sum_list([])
    0
    """
    return sum(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
