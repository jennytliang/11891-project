from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return [string for string in strings if substring in string]


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that has length in given range
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 1, 3)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : min_length <=
	"""
    return [string for string in strings if min_length <= len(string) <= max_length]


def filter_by_multiple_conditions(strings: List[str], substring: str, min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and has length in given range
    >>> filter_by_multiple_conditions([], 'a', 1, 10)
    []
    >>> filter_by_multiple_conditions(['abc', 'bacd', 'cde', 'array'], 'a', 1, 3)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in s
	and min_length <= len(s) <= max_length )
    """
    return [string for string in strings if substring in string and min_length <= len(string) <= max_length]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
