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
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else None for note in music_string.split()]


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer counting how many beats does the song last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    28
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    return sum(parse_music(music_string))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
