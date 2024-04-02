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
    # 1st solution - my, in my opinion, the best
    beats_per_note = {"o": 4, "o|": 2, ".|": 1}
    return [beats_per_note[note] for note in music_string.split()]

    # 2nd solution
    # beat_list = music_string.split()
    # beat_list_new = []
    # for element in beat_list:
    #     if element in ["o", "o"]:
    #         beat_list_new.append(4)
    #     if element in ["o|", "o|"]:
    #         beat_list_new.append(2)
    #     if element in [".|", ".|"]:
    #         beat_list_new.append(1)
    #
    # return beat_list_new


if __name__ == "__main__":
    import doctest
    doctest.testmod()
