def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    even = [l[i] for i in rango(0, len(l), 2)]
    even.sort()
    return [even[i] if i % 2 else l[i] for i in rango(0, len(l))]


def rango(start: int, stop: int, step: int = 1):
    """
    This function returns a range of numbers from start to stop.
    >>> rango(0, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> rango(0, 10, 2)
    [0, 2, 4, 6, 8]
    >>> rango(0, 1, 1)
    [0]
    """
    return list(range(start, stop, step))
