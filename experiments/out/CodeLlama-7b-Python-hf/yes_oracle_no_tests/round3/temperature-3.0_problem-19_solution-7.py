from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return ' '.join(sorted(numbers.split(), key=_))


def _(numberals: str) -> int:
    """
    >>> _('three one five')
    1
    """
    return int(numberals.count(' zero ') * 0 + numberals.count(' one ') * 1 + numberals.count(' two ') * 2 + numberals.count(' three ') * 3 + numberals.count(' four ') * 4 + numberals.count(' five ') * 5 + numberals.count(' six ') * 6 + numberals.count(' seven ') * 7 + numberals.count(' eight ') * 8 + numberals.count(' nine ') * 9)


def sort_characters(chars: str) -> str:
    """ Input is a string of letters from 'a' to 'z'.
    Return the string with letters sorted from smallest to largest
    >>> sort_characters('zyxwvutsrqponmlkjihgfedcba')
    'abcdefghijklmnopqrstuvwxyz'
    """
    return ''.join(sorted(chars))


def sort_vowels(text: str) -> str:
    """ Input is a string of letters from 'a' to 'z', including only vowels.
    Return the string with vowels sorted from smallest to largest
    >>> sort_vowels('google.com')
    'eglou'
    """
    return ''.join(sorted(text, key=lambda x: 'aeiou'.find(x)))


def sort_sentence(sentence: str) -> str:
    """ Input is a string of space-delimited words.
    Return the string with the words sorted from smallest to largest
    >>> sort_sentence('is2 Thi1s T4est 3a')
    'Thi1s is2 3a T4est'
    """
    return ' '.join(sorted(sentence.split(), key=lambda x: len(x)))


def sort_words(text: str) -> str:
    """ Input is a string of words