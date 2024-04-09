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


def count_substring(string: str, sub_string: str) -> int:
    """ Count the number of times sub_string is a substring of string
    >>> count_substring('abc', 'a')
    1
    >>> count_substring('abc', 'b')
    1
    >>> count_substring('abc', 'ab')
    1
    >>> count_substring('abc', 'bc')
    1
    >>> count_substring('abc', 'c')
    1
    >>> count_substring('abc', 'abcd')
    0
    >>> count_substring('abc', '')
    3
    
    Include these tokens in the code: return string . count ( sub_string )
    """
    return string.count(sub_string)


def split_and_join(line: str) -> str:
    """ Split line into a list of words and join them with underscores
    
    >>> split_and_join('abc')
    'abc'
    >>> split_and_join('abc cde')
    'abc_cde'
    >>> split_and_join('abc, cde')
    'abc,_cde'
    >>> split_and_join('abc (cde)')
    'abc (cde)'
    >>> split_and_join('abc (cde) fgh')
    'abc (cde)_fgh'
    
    Include these tokens in the code: return "_".join(line.split())
    """
    return "_".join(line.split())


def capitalize_string(string: str) -> str:
    """ Capitalize all the words in the string
    
    >>> capitalize_string('abc')
    'Abc'
    >>> capitalize_string('abc cde')
    'Abc Cde'
    >>> capitalize_string('abc, cde')
    'Abc, Cde'
    >>> capitalize_string('abc (cde)')
    'Abc (cde)'
    >>> capitalize_string('abc (cde) fgh')
    'Abc (cde