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



    # --------------------------------------------------------------------------
    # TODO: 2. (REPLACE THIS COMMENT WITH A WORKING IMPLEMENTATION)
    # Write an appropriate docstring for this function.
    # --------------------------------------------------------------------------


def filter_positive(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for positive integers
    >>> filter_positive([1, 2, 3, -5, 0])
    [1, 2, 3]
    >>> filter_positive([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""



    # --------------------------------------------------------------------------
    # TODO: 3. (REPLACE THIS COMMENT WITH A WORKING IMPLEMENTATION)
    # Write an appropriate docstring for this function.
    # --------------------------------------------------------------------------


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""



    # --------------------------------------------------------------------------
    # TODO: 4. (REPLACE THIS COMMENT WITH A WORKING IMPLEMENTATION)
    # Write an appropriate docstring for this function.
    # --------------------------------------------------------------------------


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans([True, False, 3.14, 5])
    [True, False