from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""


    
    return list(filter(lambda s: substring in s, strings))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
