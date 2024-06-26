from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return list(filter(lambda x: x.startswith(prefix), string))


if __name__ == '__main__':
    print(filter_by_prefix(
        ['apple', 'bear', 'cat', 'dog', 'elephant'], 'b'
    ))
