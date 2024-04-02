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
    notes = music_string.split()
    return [count_beats(note) for note in notes]


def count_beats(note: str) -> int:
    """ Return the number of beats the note lasts. """
    if note == 'o':
        return 4
    elif note == 'o|':
        return 2
    elif note == '.|':
        return 1
    else:
        raise ValueError("Invalid note " + note)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
