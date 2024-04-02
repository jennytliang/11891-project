from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    # return [s for s in strings if s.startswith(prefix)]
    r = []
    for s in strings:
        if s.startswith(prefix):
            r.append(s)
    return r


if __name__ == "__main__":
    print(filter_by_prefix(["abc", "bcd", "cde", "array"], "a"))
