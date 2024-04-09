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
    
	Include these tokens in the code: ats
	Do not include these tokens in the code: at
	"""



    def c2i(c):
        if c == 'o':
            return 4
        elif c == 'o|':
            return 2
        elif c == '.|':
            return 1
        else:
            return 0

    return [c2i(c) for c in music_string.split(' ') if c != '']


if __name__ == '__main__':
    import doctest
    doctest.testmod()
