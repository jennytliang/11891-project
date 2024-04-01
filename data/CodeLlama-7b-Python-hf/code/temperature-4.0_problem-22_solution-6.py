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
        # iterators do not need a __next_hook in python

    # Note that this method MUST be named __bool__ instead of __nonzero__, because we aim at 2.6+ version
    __bool__= None
    def __next__(self) -> int:
        for nxt in self.v_iter:  # Note that we do not stop at first found value, but rather yield all integer candidates
            if type(nxt) in (int,bool):
                return nxt
        raise StopIteration() # in python "StopIteration" is an exception which signals that we need to stop iteration/consuming
        # note that it is more idiomatic for stop_iteration to raise an appropriate type Exception, rather than just return some arbitrary object
        return None