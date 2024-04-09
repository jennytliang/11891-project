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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: whole = 4 half
	"""
    music_string = music_string.replace("o|", "o 2|")
    music_string = music_string.replace(".|", "o 1|")
    return [int(i) for i in music_string.split() if i.isdigit()]


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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: whole = 4 half = 2
	"""
    music_string = music_string.replace("o|", "o 2|")
    music_string = music_string.replace(".|", "o 1|")
    return [int(i) for i in music_string.split() if i.isdigit()]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
