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
	Do not include these tokens in the code: return [ 4 if x == '
	"""
    return [4 if x == 'o' else 2 if x == 'o|' else 1 if x == '.|' else 0 for x in music_string.split()]


def get_beat_length(beat_count: int) -> str:
    """ Input to this function is a number representing how many beats a note lasts.
    Your task is to return a string representing the note's length in seconds.

    Here is a legend:
    1 beat = 60 seconds
    2 beats = 30 seconds
    3 beats = 20 seconds
    4 beats = 15 seconds

    >>> get_beat_length(1)
    '1.0'
    >>> get_beat_length(2)
    '0.5'
    >>> get_beat_length(3)
    '0.4'
    """
    return str(beat_count / (1 if beat_count == 1 else 2 if beat_count == 2 else 3 if beat_count == 3 else 4))


def get_music_length(music_string: str) -> str:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to return a string representing the total length of music in seconds.

    Here is a legend:
    1 beat = 60 seconds
    2 beats = 30 seconds
    3 beats = 20 seconds
    4 beats = 15 seconds

    >>> get_music_length('o o| .| o| o| .| .| .| .| o o')
    '6.4'
    """
    return str(sum([1 if x == 'o' else 0.5 if x == 'o|' else 0.2 if x == '.|' else 0 for x in music_string.split()]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
