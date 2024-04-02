from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: lambda x : x . starts with ( prefix ),
	Do not include these tokens in the code: l amb das ,
	"""


    return list(f for f in strings if f.startswith(prefix))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
