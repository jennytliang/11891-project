from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return list(map(lambda x:int(x),values))

#  ******* Do Not Change the Following Line ****************
#__Z__ = filter_integers
#__Z__.__doc__ += "\n\nexample: __Z__([1, 2., 'a', 'b', 3, '', None])"
#__Z__([1, 2., 'a', 'b', 3, '', None])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)