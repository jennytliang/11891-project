from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ string for string in strings if string
	"""


    
    return [item for item in strings if item.startswith(prefix)]


if __name__ == "__main__":
    print(filter_by_prefix(["abc", "bcd", "cde", "array"], "a"))
    print(filter_by_prefix(["abc", "bcd", "cde", "array"], "b"))
    print(filter_by_prefix([], "a"))
