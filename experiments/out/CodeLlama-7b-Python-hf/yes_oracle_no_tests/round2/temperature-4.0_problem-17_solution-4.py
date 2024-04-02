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
    # parse_music('o o| .| o| o| .| .| .| .| o o')
    # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    notes = music_string.split(' ')
    result = []
    for note in notes:
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(1)
    return result


def count_beats(music_string: str) -> int:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return an integer - how many beats does the music last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> count_beats('o o| .| o| o| .| .| .| .| o o')
    40
    
	Include these tokens in the code: def count _ beats ( note : str )
	"""
    # count_beats('o o| .| o| o| .| .| .| .| o o')
    # 40
    notes = music_string.split(' ')
    result = 0
    for note in notes:
        if note == 'o':
            result += 4
        elif note == 'o|':
            result += 2
        elif note == '.|':
            result += 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
