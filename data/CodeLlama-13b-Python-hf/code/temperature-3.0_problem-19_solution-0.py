from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split() returns a list of the string, separated at each whitespace
    # map() returns the item in the list being iterated over,
    # as the function supplied to map() is applied to it
    # sort() sorts a list in ascending order
    # join() returns a string with items separated by a specified string (space in this case)
    # return statement joins the sorted string list by spaces
    return ' '.join(sorted(map(lambda x: x.lower(),
                               numbers.split(' '))))


def is_palindrome(word: str) -> bool:
    """Input is a word (string).
    Return if the word is a palindrome
    >>> is_palindrome('redder')
    True
    """
    word = word.lower()  # convert to a lower case for case-insensitive checking
    length = len(word)
    # if the length of the word is odd, check the first half against the last half
    if length % 2 == 1:
        return word[:length // 2] == word[-1:length // 2:-1]
    # otherwise, check the first half against the second half
    else:
        return word[:length // 2] == word[length // 2:]


def concatenate(strings: List[str], separator: str = '') -> str:
    """ Input is a list of strings and an optional separator
    Return one string which is a concatenation of all of the inputted strings,
    with each non-last string in the list followed by the inputted separator.
    If separator is not supplied, the strings should be concatenated with no separator.
    >>> concatenate(['I', 'like', 'italian', 'ice', 'cream'])
    'Ilikeitalianicecream'
    """
