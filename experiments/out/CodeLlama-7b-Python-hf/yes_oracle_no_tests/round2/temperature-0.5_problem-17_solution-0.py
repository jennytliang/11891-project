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
    
	Include these tokens in the code: : str ) -> int :
	Do not include these tokens in the code: ):
	"""


    def count_beat(music_string):
        """
        This function is used to count the number of beats for each note.
        """
        whole_note = 4
        half_note = 2
        quarter_note = 1
        whole_count = 0
        half_count = 0
        quarter_count = 0
        for i in range(len(music_string)):
            if music_string[i] == 'o':
                whole_count += whole_note
            elif music_string[i] == 'o|':
                half_count += half_note
            elif music_string[i] == '.|':
                quarter_count += quarter_note
            else:
                continue
        return [whole_count, half_count, quarter_count]

    def split_string(music_string):
        """
        This function is used to split the string into a list of notes.
        """
        return music_string.split()

    def count_beat_list(music_list):
        """
        This function is used to count the number of beats for each note in the list.
        """
        whole_note = 4
        half_note = 2
        quarter_note = 1
        whole_count = 0
        half_count = 0
        quarter_count = 0
        for i in range(len(music_list)):
            if music_list[i] == 'o':
                whole_count += whole_note
            elif music_list[i] == 'o|':
                half_count += half_note
            elif music_list[i] == '.|':
                quarter_count += quarter_note
            else:
                continue
        return [whole_count, half_count, quarter_count]

    def convert_list_to_int(music_list):
        """
        This function is used to convert the list to a list of integers.
        """
        return [int(i) for i in music_list]

    def convert_list_to_string(music_list):
        """
        This function is used to convert the list to a