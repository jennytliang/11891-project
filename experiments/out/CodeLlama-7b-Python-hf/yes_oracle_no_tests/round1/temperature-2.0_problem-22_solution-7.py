from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = list(filter(lambda x: isinstance(x, int), values))
    return r


if __name__ == '__main__':
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], filter_integers(
        [1, 2, 3, 'abc', {}, []])
    assert filter_integers(['a', 3.14, 5]) == [5], filter_integers(['a', 3.14, 5])
    assert filter_integers([]) == [], filter_integers([])
    assert filter_integers([1, 1.0, 1, 1 + 0j]) == [1, 1, 1], filter_integers([1, 1.0, 1, 1 + 0j])
    print('Done')
