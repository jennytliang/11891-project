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
	Do not include these tokens in the code: music
	"""
    return [4 if x == 'o' else 2 if x == 'o|' else 1 if x == '.|' else 0 for x in music_string]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return number of beats in the song.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    32
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: music
	"""
    return sum([4 if x == 'o' else 2 if x == 'o|' else 1 if x == '.|' else 0 for x in music_string])


def count_beats_2(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return number of beats in the song.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats_2('o o| .| o| o| .| .| .| .| o o')
    32
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: music
	"""
    return music_string.count('o') * 4 + music_string.count('o|') * 2 + music_string.count('.|')


def count_beats_3(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your