from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return [s for s in strings if substring in s]


def filter_by_substring_with_lambda(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_with_lambda([], 'a')
    []
    >>> filter_by_substring_with_lambda(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return list(filter(lambda s: substring in s, strings))


if __name__ == '__main__':
    import doctest

    doctest.testmod()