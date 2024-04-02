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

    r = [i for i in values if type(i) == int]
    return r


def multiply_by_five(value: int) -> int:
    """Multiplies given integer by 5
    >>> multiply_by_five(9)
    45
    >>> multiply_by_five(8)
    40

	Include these tokens in the code: if ( int ( ) ( )
	Do not include these tokens in the code: * % 
	"""

    return int(str(value*5))


def print_all_values(values: List[int]) -> None:
    """Print all array values
    >>> print_all_values([7,2,3])
    7
    2
    3    
    
	Include these tokens in the code: ' ' .join [ for
	Do not include these tokens in the code: print list ( * 
	"""
    values = [multiply_by_five(value) for value in values for num in range(value)]
    return values


if __name__ == '__main__':
    import doctest
    doctest.testmod()
