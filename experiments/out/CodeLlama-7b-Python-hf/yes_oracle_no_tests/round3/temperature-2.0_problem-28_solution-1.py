from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: " ". join ( strings )
	Do not include these tokens in the code: r
	"""

    r = " ".join(strings)
    return r


def capitalize_first_letter(word: str) -> str:
    """Capitalize first letter
	
	>>> capitalize_first_letter('python')
	'Python'
    >>> capitalize_first_letter('java')
    'Java'
    """

    return word[0].upper() + word[1:]


def capitalize_all_letters(word: str) -> str:
    """Capitalize all letters
	>>> capitalize_all_letters('python')
	'Python'
    >>> capitalize_all_letters('java')
    'Java'
    """

    return word.upper()


def lowercase_all_letters(word: str) -> str:
    """Lowercase all letters
	>>> lowercase_all_letters('Python')
	'python'
    >>> lowercase_all_letters('Java')
    'java'
    """

    return word.lower()


def swap_first_two_characters(word: str) -> str:
    """Swap first two characters
	>>> swap_first_two_characters('Python')
	'ThonPython'
    >>> swap_first_two_characters('Java')
    'Java'
    """

    return word[1:] + word[0]


def reverse_word(word: str) -> str:
    """Reverse word
	>>> reverse_word('Python')
	'nohtyP'
    >>> reverse_word('Java')
    'avaja'
    """

    return word[::-1]


def reverse_string(word: str) -> str:
    """Reverse string
    >>> reverse_string('Python')
    'nohtyP'
    >>> reverse_string('Java')
    'avaja'
    """

    return word[::-1]


def replace_characters(word: str, old_char: str, new_char: str) -> str:
    """Replace characters
    >>> replace_characters