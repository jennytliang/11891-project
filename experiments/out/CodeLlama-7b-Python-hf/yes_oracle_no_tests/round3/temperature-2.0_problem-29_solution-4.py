from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: #
	"""
    return [x for x in strings if x.startswith(prefix)]


if __name__ == "__main__":
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
