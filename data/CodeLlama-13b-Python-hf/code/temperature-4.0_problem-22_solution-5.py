from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

    even_numbers: List[int] = []
    for i in values:
        if type(i) == int:
            even_numbers += [i] if i % 2 == 0 else []
    # return even_numbers

@filter_values
def filter_values(array, type):
     filter_val = list(x for x in range(array.size()) if type(array[i]))
