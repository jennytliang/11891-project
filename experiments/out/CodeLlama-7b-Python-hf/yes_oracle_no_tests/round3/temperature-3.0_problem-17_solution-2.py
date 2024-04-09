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
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: return [ 4 if note == '
	"""
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else 0 for note in music_string.split()]


def validate_music(music_string: str) -> bool:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to validate if the string is a valid musical notation.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> validate_music('o o| .| o| o| .| .| .| .| o o')
    True
    >>> validate_music('o o| .| o| o| .| .| .| .| o o|')
    False
    >>> validate_music('o o| .| o| o| .| .| .| .| o o| o o| .| o|')
    True
    
	Include these tokens in the code: def validate
	Do not include these tokens in the code: return
	"""
    return all([note == 'o' or note == 'o|' or note == '.|' for note in music_string.split()])


def count_music(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to count how many beats does the music last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_music('o o| .| o| o| .| .| .| .| o o')
    20
    >>> count_music('o o| .| o| o| .| .| .| .| o o|')
    0
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: return
	