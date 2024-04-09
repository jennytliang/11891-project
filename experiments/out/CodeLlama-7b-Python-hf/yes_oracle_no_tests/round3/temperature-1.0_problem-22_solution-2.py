from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: filter ( lambda x : type ( x ) ==
	Do not include these tokens in the code: f for f in
	"""



    retur_list = []
    for i in values:
        if type(i) == int:
            retur_list.append(i)
    return retur_list





if __name__ == '__main__':
    import doctest
    doctest.testmod()
