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

    r_list = [] # filtered list result initialized as an empty list

    for item in values:
        if item%1 == 0: # if value is intigeter
            r_list.append(item) # append to result list
    return r_list

# Pybites solution

def filter_integers1(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
	>>> filter_integers(['a', 3.14, 5])
	[5]
	>>> filter_integers([1, 2, 3, 'abc', {}, []])
	[1, 2, 3]
    
    """
    r_list = [] # initialize empty list of integers = [int(v) for v in values
                # if type(v) == int]
    try:        
        for val in values:
            int(val)+1 # if value fails to be added with +1 ValueError will occur
            r_list.append(val) # adds an item to the list
    except ValueError:
        pass # doesn't append the val
    return r_list # return filtered integers from list

# Pybites solution

def filter_integers2(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers

	>>> filter_integers(['a', 3.14, 5])
	[5]
	>>> filter_integers([1, 2, 3, 'abc', {}, []])
	[1, 2, 3]
    
    """
    return [int(v) if isinstance(v,float) else int(v) for v in values if int(v)+1 == int(v)+1]
    
