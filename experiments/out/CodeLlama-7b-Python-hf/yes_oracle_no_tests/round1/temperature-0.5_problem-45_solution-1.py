def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    return a * h / 2


d = {"a": 1, "b": 2, "c": 3}


def d_keys(d):
    """Given a dictionary d, return the keys of d in a list.
    >>> d_keys(d)
    ['a', 'b', 'c']
    """
    keys = []
    for key in d:
        keys.append(key)
    return keys


def d_values(d):
    """Given a dictionary d, return the values of d in a list.
    >>> d_values(d)
    [1, 2, 3]
    """
    values = []
    for value in d.values():
        values.append(value)
    return values


def d_items(d):
    """Given a dictionary d, return the items of d in a list.
    >>> d_items(d)
    [('a', 1), ('b', 2), ('c', 3)]
    """
    items = []
    for key, value in d.items():
        items.append((key, value))
    return items


def d_get(d, key):
    """Given a dictionary d and a key, return the value associated with that key.
    >>> d_get(d, 'a')
    1
    """
    return d[key]


def d_pop(d, key):
    """Given a dictionary d and a key, remove that key from d. 
    Return the value associated with that key.
    >>> d_pop(d, 'a')
    1
    >>> d
    {'b': 2, 'c': 3}
    """
    value = d[key]
    del d[key]
    return value


def d_clear(d):
    """Given a dictionary d, remove all the items from it.
    >>> d_clear(d)
    >>> d
    {}
    """
    d.clear()


def d_update(d1, d2):
    """Given two dictionaries d1 and d2, update d1 with the items