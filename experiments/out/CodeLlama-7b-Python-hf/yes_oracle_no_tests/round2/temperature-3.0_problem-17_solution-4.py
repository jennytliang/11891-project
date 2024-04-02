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
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else None for note in music_string.split()]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return number of beats in the song.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    32
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    return sum(parse_music(music_string))


def count_down(count: int) -> str:
    """ Write a function that takes an integer and returns a string with a counting down message.
    For example, for count = 3 it should return "3, 2, 1... zero".

    >>> count_down(3)
    '3, 2, 1... zero'
    
	Include these tokens in the code: def count _ down ( count : int )
	"""
    return ', '.join(map(str, range(count, 0, -1))) + '... zero'


def count_down_by(count: int, by: int) -> str:
    """ Write a function that takes an integer count and an integer by and returns a string with a counting down message.
    For example, for count = 3 and by = 2 it should return "3, 1, -1... zero".

    >>> count_down_by(3, 2)
    '3, 1, -1... zero'
    
	Include these tokens in the code: def count _ down _ by ( count : int, by : int )
	"""
    return ', '.join(map(str, range(count,