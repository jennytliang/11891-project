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
    return [4 if token == 'o' else 2 if token == 'o|' else 1 if token == '.|' else 0
            for token in music_string.split()]


def count_notes(music_string: str, note_type: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to count how many times the given note_type is present in the string.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_notes('o o| .| o| o| .| .| .| .| o o', 'o')
    2
    >>> count_notes('o o| .| o| o| .| .| .| .| o o', 'o|')
    2
    >>> count_notes('o o| .| o| o| .| .| .| .| o o', '.|')
    3
    
	Include these tokens in the code: def count _ notes ( note : str )
	"""
    return music_string.count(note_type)


def count_all_notes(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to count how many times each note type is present in the string.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_all_notes('o o| .| o| o| .| .| .| .| o o')
    [2, 2, 3, 4]
    
	Include these tokens in the code: def count _ all _ notes ( note : str )
	"""
    return [music_string.count('o'), music_string.count('o|'), music_string