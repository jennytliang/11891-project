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


def count_substring(string: str, substring: str) -> int:
    """Count the number of times substring is in string
    >>> count_substring('', '')
    0
    >>> count_substring('word', '')
    1
    >>> count_substring('word', 'o')
    1
    >>> count_substring('word', 'w')
    1
    >>> count_substring('word', 'wo')
    1
    >>> count_substring('word', 'wor')
    1
    >>> count_substring('word', 'word')
    1
    >>> count_substring('word', 'rd')
    1
    >>> count_substring('word', 'd')
    1
    >>> count_substring('word', 'or')
    0
    >>> count_substring('word', 'od')
    0
    >>> count_substring('word', 'o')
    1
    >>> count_substring('word', 'r')
    0
    >>> count_substring('word', 'w')
    1
    >>> count_substring('word', 'd')
    1
    >>> count_substring('word', 'wo')
    1
    >>> count_substring('word', 'woo')
    0
    >>> count_substring('word', 'wood')
    0
    """
    return string.count(substring)


def before_after_all(string: str, substring: str) -> str:
    """Return string where all occurrences of substring are surrounded by '<bef> <aft>'
    >>> before_after_all('word', '')
    'word'
    >>> before_after_all('word', 'w')
    '<bef>w<aft>ord<bef>w<aft>'
    >>> before_after_all('word', 'o')
    'w<bef>or<aft>d'
    >>> before_after_all('word', 'rd')
    'wo<bef>rd<aft>'
    >>> before_after_all('word', 'd')
    'wo<bef>rd'
    >>> before_after_all('word', '