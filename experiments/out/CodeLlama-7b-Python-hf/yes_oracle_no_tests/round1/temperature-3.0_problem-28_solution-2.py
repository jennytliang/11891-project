from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_word_and_number(word: str, number: int) -> str:
    """ Concatenate word and number into a single string
    >>> concatenate_word_and_number('a', 1)
    'a1'
    >>> concatenate_word_and_number('a', 0)
    'a0'
    >>> concatenate_word_and_number('a', -1)
    'a-1'
    
	Include these tokens in the code: return word + str ( number )
	Do not include these tokens in the code: result : str = ""
	"""
    return word + str(number)


def concatenate_word_and_number_as_string(word: str, number: int) -> str:
    """ Concatenate word and number into a single string
    >>> concatenate_word_and_number_as_string('a', 1)
    'a1'
    >>> concatenate_word_and_number_as_string('a', 0)
    'a0'
    >>> concatenate_word_and_number_as_string('a', -1)
    'a-1'
    
	Include these tokens in the code: return word + str ( number )
	Do not include these tokens in the code: result : str = ""
	"""
    return word + str(number)


def concatenate_with_separator(strings: List[str], separator: str = ",") -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_with_separator([])
    ''
    >>> concatenate_with_separator(['a', 'b', 'c'])
    'a,b,c'
    >>> concatenate_with_separator(['a', 'b', 'c'], separator = ':')
    'a:b:c'
    
	Include these tokens in the code: return separator . join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return separator.join(strings)


def concaten