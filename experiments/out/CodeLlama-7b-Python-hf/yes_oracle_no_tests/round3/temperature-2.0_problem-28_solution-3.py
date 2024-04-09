from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def count_characters(text: str) -> int:
    """ Count number of characters in a text
    >>> count_characters('')
    0
    >>> count_characters('abc')
    3
    >>> count_characters('abcdef')
    6
    
	Include these tokens in the code: return len ( text )
	"""
    return len(text)


def count_words(text: str) -> int:
    """ Count number of words in a text
    >>> count_words('')
    0
    >>> count_words('abc')
    1
    >>> count_words('abc def')
    2
    >>> count_words('abc def ghi')
    3
    
	Include these tokens in the code: return len ( text. split () )
	"""
    return len(text.split())


def list_to_string(items: List[str]) -> str:
    """ Convert list of strings into a single string
    >>> list_to_string([])
    ''
    >>> list_to_string(['a', 'b', 'c'])
    'a b c'
    >>> list_to_string(['abc', 'def'])
    'abc def'
    
	Include these tokens in the code: return " ". join ( items )
	"""
    return " ".join(items)


def reverse_string(text: str) -> str:
    """ Reverse the order of the characters in a string
    >>> reverse_string('')
    ''
    >>> reverse_string('abc')
    'cba'
    >>> reverse_string('Python')
    'nohtyP'
    
	Include these tokens in the code: return text [ :: -1]
	"""
    return text[::-1]


def remove_first_word(text: str) -> str:
    """ Remove first word from a text
    >>> remove_first_word('')
    ''
    >>> remove_first_word('abc')
    'abc'
    >>> remove_first_word('abc def')
    'def'