from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(l -> starts_with(l, prefix), strings))


print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 's'))
