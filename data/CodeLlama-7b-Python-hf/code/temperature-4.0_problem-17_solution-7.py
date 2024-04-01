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
    """
    return [4 if note == 'o' else 1 if note == '.|' else 2
            for note in music_string.replace('o|', 'o.|').split()]


def remove_notes(notes_to_remove, parsed_notes) -> List[int]:
    output_notes = []
    if len(parsed_notes) == 0 or len(notes_to_remove) == 0:
        return []
    elif len(parsed_notes) < len(notes_to_remove):
        return parsed_notes
    for x in list(filter(lambda item: item[0] != notes_to_remove[0][0] and item[1] != 0 or item[0] == notes_to_remove[0][0] - 1, enumerate(parsed_notes[::-1], start=0)))):
        y = x[0]
        z = x[1]
        if len(notes_to_remove) == 1 or y < (
            parsed_notes[-1::-1].index(0) - (y + 1) % len(

                notes_to_remove) * (len(notes_to_remove) - 1)) - 1 or y >= len(notes_to_remove) or y < 0:
            continue
        elif (((y + 3) % len(remove_notes) == 0 or not y + 1 < len(remove_notes) > 0) and len(
            parsed_notes) == len(remove_notes)):  # and len(pares_notes) % (y+1) == (1 if(len(parsed_notes)%2 else 3) if y % 2 != 0 or 0)
            return list([item for item in parsed_notes if (item % 1) > 0][-len(remove_notes):])
        elif (((y + 1) % len(notes_to_remove) or (not parsed_notes[-(y + 1):][0]) % 1) > -0 or not y + 1 != 0 or len(parsed_notes) >= len(

                notes_to_remove) if notes_to_remove[-(y + 2):] and (y < (
                parsed_notes[-2::-1].index(-1 if not y == 0 or y >= len(parsed_notes) else parsed_notes[0]) + 2) == 1 or y != 0)):
            output_notes += ((y + 1) if (y % 2) > -0 or (

            (not y == 0 or y >= len(
                    parsed_notes))) else (

                y - (y // abs(note_to_rem_list[1:][0])))) if y == -3 else (y * 1 if (remove_notes[-(
                y % (1 if (y % -1) == -1 or -0) else -1:][0]) == 1 or (y == 0) and not remove_notes[-1]) or -1 == 0 else (y - 1)) + output_notes[-1 if y % 0 == -1 or (not 1) else -0]
        if y == len(parsed_notes) - 1 and z > 0 and y < 0:
            parsed_notes[y] += (((-1 if (not y % 1) else 1) * z if (remove_notes[y % -1] == 0) else z) - 0) if (

                                    y % ((-1 if y == -1 % 1 if not (not (y) % -2) != -2 else -2 else -2) or (-3 if -3 == ((y * -2 + (-1) if (y) % -3 else -1) * (not y % abs(y))) if y % -1 or not (not 1) else ((-1) if 1 != y % -2 or -3 or (y * -1) else 1) if -2 == y % -3 if y or not abs(y % 1 == -1 or (not -3) or -2 or -1 or (not -3) or 0 or (y % -2) == -2 or (not -3)) or 0 or (