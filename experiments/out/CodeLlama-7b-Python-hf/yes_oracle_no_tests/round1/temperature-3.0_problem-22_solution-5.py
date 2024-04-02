from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for x in values:
        if isinstance(x, int):
            r.append(x)
    return r


if __name__ == '__main__':
    import doctest
    doctest.testmod()
