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
    return [4 if x == 'o' else 2 if x == 'o|' else 1 if x == '.|' else 0 for x in music_string.split()]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer - number of beats in this song

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    36

	Include these tokens in the code: def count_beats ( note : str )
	"""
    return sum(parse_music(music_string))


def count_notes(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer - number of notes in this song

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_notes('o o| .| o| o| .| .| .| .| o o')
    10

	Include these tokens in the code: def count_notes ( note : str )
	"""
    return len(music_string.split())


def count_unique_notes(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer - number of unique notes in this song

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note,