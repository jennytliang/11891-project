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


    def str_to_list(music_string: str, token: str) -> List[int]:
        """ Helper function that returns a list of integers
        representing how many beats each note lasts """
        return [int(note.count(token)/2) for note in music_string.split()]

    def parse_music(music_string: str) -> List[int]:
        """ Returns a list of integers representing how many beats each note lasts """
        return str_to_list(music_string, 'o') + str_to_list(music_string, 'o|') + str_to_list(music_string, '.|')

    return parse_music(music_string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
