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
    list_of_music = music_string.split()
    list_of_beats = []
    for note in list_of_music:
        if note == 'o':
            list_of_beats.append(4)
        elif note == 'o|':
            list_of_beats.append(2)
        elif note == '.|':
            list_of_beats.append(1)
    return list_of_beats


def parse_music_2(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music_2('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    list_of_music = music_string.split()
    list_of_beats = []
    for note in list_of_music:
        if note == 'o':
            list_of_beats.append(4)
        elif note == 'o|':
            list_of_beats.append(2)
        elif note == '.|':
            list_of_beats.append(1)
    return list_of_beats


def parse_music_3(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
