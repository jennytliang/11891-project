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
    # return []
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else 0 for note in music_string.split()]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return the total number of beats.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    20
    >>> count_beats('o o| .| o| o| .| .| .| .| o o| .|')
    21
    """
    # return 0
    return sum(parse_music(music_string))


def count_unique_notes(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return the number of unique notes used.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_unique_notes('o o| .| o| o| .| .| .| .| o o')
    7
    >>> count_unique_notes('o o| .| o| o| .| .| .| .| o o| .|')
    8
    """
    # return 0
    return len(set(music_string.split()))


def count_max_consecutive_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return the maximum number of consecutive be