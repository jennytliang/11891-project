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

    def  parse_note(note_string):
        if note_string == 'o':
            return 4
        elif note_string == 'o|':
            return 2
        elif note_string == '.|':
            return 1
        else:
            raise ValueError(f'Invalid note: {note_string}')

    music_string = music_string.replace("o", "o ")
    music_string = music_string.replace("o|", "o| ")
    music_string = music_string.replace(".|", ".| ")
    music_string = music_string.replace("  ", " ")
    music_string = music_string.strip()

    return [parse_note(note) for note in music_string.split(" ")]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
