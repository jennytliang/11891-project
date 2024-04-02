from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: if len
	"""
    return " ".join(strings)


def concatenate_with_spaces(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with spaces between them
    >>> concatenate_with_spaces([])
    ''
    >>> concatenate_with_spaces(['a', 'b', 'c'])
    'a b c'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: if len
	"""
    return " ".join(strings)


def concatenate_with_commas(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas between them
    >>> concatenate_with_commas([])
    ''
    >>> concatenate_with_commas(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: return ", ". join
	Do not include these tokens in the code: if len
	"""
    return ", ".join(strings)


def concatenate_with_and(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas between them
    and "and" before the last item
    >>> concatenate_with_and([])
    ''
    >>> concatenate_with_and(['a', 'b', 'c'])
    'a, b and c'
    >>> concatenate_with_and(['a'])
    'a'
    
	Include these tokens in the code: return " and ". join
	Do not include these tokens in the code: if len
    """
    if len(strings) == 1:
        return strings[0]

    return ", ".join(strings[:-1]) + " and " + strings[-1]


def count_letters(string: str) -> int:
    """ Count number of letters in a string
    >>> count_letters("abc")
    3
    >>> count_letters("aabbcc")
    6
    >>> count_letters("")
    0
    """
    return len(