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


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return the total number of beats in the song.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    32
    
	Include these tokens in the code: def count_beats ( note : str )
	"""
    return sum(parse_music(music_string))


def split_music(music_string: str) -> List[str]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of songs.
    A song is a string in the same format, but without the dots.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> split_music('o o| .| o| o| .| .| .| .| o o')
    ['o o| ', 'o| ', 'o| ', 'o| ', ' ', ' ', ' ', ' ', 'o o']

	Include these tokens in the code: def split_music ( note : str )
	"""
    return [note for note in music_string.split() if note != '.|']


def count_unique_notes(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return the number of unique