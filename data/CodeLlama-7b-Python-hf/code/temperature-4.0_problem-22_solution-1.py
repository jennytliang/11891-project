from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

    return list(FilterIntegersContext(values))


class FilterIntegersContext:
    """ Iterator wrapper class

    >>> list(FilterIntegersContext([1, "A", 2.8, "B", '5' , 42, '6.9'])) # [5] will be filtered out
    [5] (will be [])

    >>> f_int=FilterIntegers() # filter context can be created once and applied to different values
    >>> f_int('A', 500, .001)  # f_int(42) returns the next item of underlying iterator
    3.0
    >>> next(f_int)             # next returns the next available item
    5

    """
    def __init__(self,values):
        self.v_iter = iter(values)
        print("Hello world!")

    def __iter__(self) -> 'FilterIntegersContext':
        return self


