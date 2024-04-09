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
    
	Include these tokens in the code: _ be ats
	"""


    def parse_token(token: str):
        if token == 'o':
            return 4
        elif token == 'o|':
            return 2
        elif token == '.|':
            return 1
        else:
            raise ValueError(f'Unrecognized token: {token}')

    tokens = music_string.split()
    return [parse_token(token) for token in tokens]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
