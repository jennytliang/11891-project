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


    def get_beats(music_string: str) -> List[int]:
        """
        This function takes a string of musical notes and returns a list of integers representing how long each note
        lasts.
        """
        # Initialize variables
        beat_list = []
        beat_map = {'o': 4, 'o|': 2, '.|': 1}

        # Iterate through the string
        for note in music_string:
            beat_list.append(beat_map[note])

        return beat_list

    return get_beats(music_string)


def parse_music_one_liner(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music_one_liner('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
	Include these tokens in the code: _ be ats
	"""

    return [4 if note == 'o' else 2 if note == 'o|' else 1 for note in music_string.split()]


def parse_music_comprehension(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts