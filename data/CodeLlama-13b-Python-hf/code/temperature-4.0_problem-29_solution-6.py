from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


METADATA = {'author': 'jt', 'dataset': 'test'}

def find_longest_string(strings: List[str]) -> str:
    strings.sort(key = lambda x: int(len(x) >= 14))
    strings1 = strings[-4:]
    string3 = strings1[-1].upper()
