from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for s in strings:
        ret += s
    return ret


def count_letters(string: str) -> int:
    """ Count how many letters are in a string
    >>> count_letters("")
    0
    >>> count_letters("abc")
    3
    >>> count_letters("aabbccee")
    5
    
	Include these tokens in the code: ".
	"""

    ret = 0
    for s in string:
        if s.isalpha():
            ret += 1
    return ret


def count_vowels(string: str) -> int:
    """ Count how many vowels are in a string
    >>> count_vowels("")
    0
    >>> count_vowels("abc")
    0
    >>> count_vowels("aabbccee")
    5
    
	Include these tokens in the code: ".
	"""

    ret = 0
    for s in string:
        if s in "aeiou":
            ret += 1
    return ret


def count_consonants(string: str) -> int:
    """ Count how many consonants are in a string
    >>> count_consonants("")
    0
    >>> count_consonants("abc")
    3
    >>> count_consonants("aabbccee")
    4
    
	Include these tokens in the code: ".
	"""

    ret = 0
    for s in string:
        if s in "bcdfghjklmnpqrstvwxz":
            ret += 1
    return ret


def count_punctuation(string: str) -> int:
    """ Count how many punctuation marks are in a string
    >>> count_punctuation("")
    0
    >>> count_punctuation("abc")
    0
    >>> count_punctuation("aabbccee")
    0
    >>> count_punctuation("abc.def!ghi")
    2
    
	Include