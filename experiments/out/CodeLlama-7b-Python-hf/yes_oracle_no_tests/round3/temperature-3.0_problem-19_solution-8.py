from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted([int(x) for x in numbers.split()]))


def count_letters(text: str) -> str:
    """ Return a string with letters and their counts
    >>> count_letters('aaabbc')
    'a:3 b:2 c:1'
    """
    return f"{text.count('a')}a{text.count('b')}b{text.count('c')}c"


def remove_duplicates(text: str) -> str:
    """ Return a string with only unique characters
    >>> remove_duplicates('abbc')
    'abc'
    """
    return "".join(set(text))


def remove_vowels(text: str) -> str:
    """ Return a string with all the vowels removed
    >>> remove_vowels('abcdefghijklmnopqrstuvwxyz')
    'bcdfghjklmnpqrstwxyz'
    """
    return "".join([x for x in text if x not in "aeiou"])


def remove_duplicate_words(text: str) -> str:
    """ Return a string with only unique words
    >>> remove_duplicate_words('Mississippi')
    'Mississippi'
    """
    return " ".join(set(text.split()))


def find_vowels(text: str) -> str:
    """ Return a string with all the vowels
    >>> find_vowels('abcdefghijklmnopqrstuvwxyz')
    'aeiou'
    """
    return "".join([x for x in text if x in "aeiou"])


def replace_letters(text: str) -> str:
    """ Return a string with all the vowels replaced with '*'
    >>> replace_letters('abcdefghijklmnopqrstuvwxyz')
    '******f******g******h******i******j******k******l******m******n******o******p******q******