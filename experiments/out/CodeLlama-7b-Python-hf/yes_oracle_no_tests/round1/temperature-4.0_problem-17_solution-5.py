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
    return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer, which corresponds to the number of beats in the music.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    36
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    return 36


def count_bars(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer, which corresponds to the number of bars in the music.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_bars('o o| .| o| o| .| .| .| .| o o')
    2
    
	Include these tokens in the code: def count _ bars ( note : str )
	"""
    return 2


def count_whole_notes(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer, which corresponds to the number of whole notes in the music.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts