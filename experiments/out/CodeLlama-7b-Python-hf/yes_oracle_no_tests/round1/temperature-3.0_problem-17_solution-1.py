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
    return [4 if i == 'o' else 2 if i == 'o|' else 1 if i == '.|' else 0 for i in music_string.split()]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
