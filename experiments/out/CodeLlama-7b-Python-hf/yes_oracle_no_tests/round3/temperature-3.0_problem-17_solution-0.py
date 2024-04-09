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
    
	Include these tokens in the code: count
	Do not include these tokens in the code: str
	"""



    count = []
    for i in music_string.split():
        if i == 'o':
            count.append(4)
        elif i == 'o|':
            count.append(2)
        elif i == '.|':
            count.append(1)
    return count


def main():
    print("Input your music:")
    music_string = input()
    print(parse_music(music_string))


if __name__ == "__main__":
    main()