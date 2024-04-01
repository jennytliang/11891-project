from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

def filter_positive_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any Python values only for positive integers
    >>> filter_positive_integers(['a', 3.14, 5, -10])
    []
    >>> filter_positive_integers([1, -2, 3, 'abc', {}, []])
    [1]
    """
