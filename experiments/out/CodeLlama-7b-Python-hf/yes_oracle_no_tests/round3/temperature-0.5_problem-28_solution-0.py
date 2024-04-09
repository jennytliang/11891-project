from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: st ri for stri in
	"""



    return "".join(strings)


def count_letters(word: str) -> int:
    """ Count letters in a given string
    >>> count_letters('')
    0
    >>> count_letters('abc')
    3
    >>> count_letters('aabbcc')
    6
    
	Include these tokens in the code: word, letters
	Do not include these tokens in the code: letters = 0, loop, for
    """



    return len(word)


def count_unique_letters(word: str) -> int:
	""" Count unique letters in a given string
    >>> count_unique_letters('')
    0
    >>> count_unique_letters('abc')
    3
    >>> count_unique_letters('aabbcc')
    3
    
	Include these tokens in the code: word, letters
	Do not include these tokens in the code: letters = 0, loop, for, if
    """



    return len(set(word))


def count_vowels(word: str) -> int:
    """ Count the number of vowels in a given string
    >>> count_vowels('')
    0
    >>> count_vowels('abc')
    0
    >>> count_vowels('aabbcc')
    0
    >>> count_vowels('aAeEiIoOuU')
    5
    
	Include these tokens in the code: word, vowels
	Do not include these tokens in the code: vowels = 0, loop, for, if
    """



    return len([letter for letter in word if letter in "aeiou"])


def count_consonants(word: str) -> int:
    """ Count the number of consonants in a given string
    >>> count_consonants('')
    0
    >>> count_consonants('abc')
    3
    >>> count_consonants('aabbcc')
    6
    >>> count_consonants('aAeEiIoOuU')
    0
    