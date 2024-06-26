from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Do not include these tokens in the code: r = [ i for i
	"""
    return [i for i in values if type(i) == int]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
