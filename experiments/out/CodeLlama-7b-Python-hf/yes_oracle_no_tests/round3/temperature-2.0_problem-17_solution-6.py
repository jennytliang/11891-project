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
    return [4 if i == 'o' else 2 if i == 'o|' else 1 if i == '.|' else 0 for i in music_string.split()]


def find_min_max(numbers: List[int]) -> str:
    """ This function takes a list of numbers and returns a string with the minimum and maximum numbers.

    >>> find_min_max([1, 2, 3, 4, 5])
    'The minimum number is 1 and the maximum number is 5'
    
	Include these tokens in the code: def find_min_max ( numbers : list )
	"""
    return f"The minimum number is {min(numbers)} and the maximum number is {max(numbers)}"


def get_average(numbers: List[float]) -> float:
    """ This function takes a list of numbers and returns a string with the average of the numbers.

    >>> get_average([1, 2, 3, 4, 5])
    'The average is 3'
    
	Include these tokens in the code: def get_average ( numbers : list )
	"""
    return f"The average is {sum(numbers) / len(numbers)}"


def get_length(s: str) -> int:
    """ This function takes a string and returns the length of the string.

    >>> get_length("Hello, World!")
    12
    
	Include these tokens in the code: def get_length ( s : str )
	"""
    return len(s)


def get_last_char(s: str) -> str:
    """ This function takes a string and returns the last character of the string.

    >>> get_last_char("Hello, World!")
    '!'
    
	Include these tokens in the code: def get_last_char ( s : str )
	"""
    return s[-1]


def get_last_n_chars(s: str, n: int) -> str:
    """ This function takes a string and returns the last n characters of the string.

    >>>