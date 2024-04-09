from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: r = "" for s
	"""
    # r = ""
    # for s in strings:
    #     r += s
    # return r
    return "".join(strings)


def count_letters(s: str) -> int:
    """ Count letters in string
    >>> count_letters("")
    0
    >>> count_letters("abc")
    3
    >>> count_letters("aabbcc")
    6
    """
    return len(s)


def count_letters_different(s: str) -> int:
    """ Count different letters in string
    >>> count_letters_different("")
    0
    >>> count_letters_different("abc")
    3
    >>> count_letters_different("aabbcc")
    3
    """
    return len(set(s))


def count_vowels(s: str) -> int:
    """ Count vowels in string
    >>> count_vowels("")
    0
    >>> count_vowels("abc")
    1
    >>> count_vowels("aabbcc")
    2
    """
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
    return count


def count_consecutive_vowels(s: str) -> int:
    """ Count consecutive vowels in string
    >>> count_consecutive_vowels("")
    0
    >>> count_consecutive_vowels("abc")
    0
    >>> count_consecutive_vowels("aabbcc")
    0
    >>> count_consecutive_vowels("aei")
    2
    >>> count_consecutive_vowels("aaei")
    3
    >>> count_consecutive_vowels("aaeiiii")
    3
    >>> count_consecutive_vowels("aaeiiiii")
    4
    """
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
