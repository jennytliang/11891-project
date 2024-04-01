from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    # split string into list of words
    word_list: List[str] = numbers.split()

    # split each word into a list of letters
    letter_list: List[List[str]] = []
    for word in word_list:
        letter_list.append(list(word))

    # convert letters to integers
    int_list: List[List[int]] = []
    for letters in letter_list:
        int_list.append(convert_letters(letters))

    # sort integers
    int_list.sort()

    # convert integers back to letters
    sorted_list: List[List[str]] = []
    for ints in int_list:
        sorted_list.append(convert_ints(ints))

    # convert list of lists back to a single list
    sorted_words = " ".join(convert_lists(sorted_list))

    return sorted_words


def convert_letters(letters: List[str]) -> List[int]:
    """ Convert a list of letters to a list of integers
    >>> convert_letters(['o', 'n', 'e'])
    [1, 5, 3]
    """
    int_list: List[int] = []
    for letter in letters:
        int_list.append(convert_letter(letter))
    return int_list


def convert_letter(letter: str) -> int:
    """ Convert a single letter to an integer
    >>> convert_letter('o')
    1
    """
    if letter == "zero":
        return 0
    elif letter == "one":
        return 1
    elif letter == "two":
        return 2
    elif letter == "three":
        return 3
    elif letter == "four":
        return 4
    elif letter == "five":
        return 5
    elif letter == "six":
        return 6
    elif letter == "seven":
        return 7
    elif letter == "eight":
        return 8
    elif letter == "nine":
        return 9
    else:
        return -