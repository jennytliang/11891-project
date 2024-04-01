def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    return a * h / 2


d = {
    "name": "d",
    "age": 10,
    "hobby": "programming",
    "fav_nums": [1, 2, 3],
    "fav_colors": {"blue", "red", "green"},
    "fav_foods": {"pizza", "ice cream", "chocolate"},
}


def get_item(dictionary, key):
    """Given a dictionary and a key return the value for the key.
    >>> get_item(d, "name")
    'd'
    >>> get_item(d, "age")
    10
    >>> get_item(d, "hobby")
    'programming'
    >>> get_item(d, "fav_nums")
    [1, 2, 3]
    >>> get_item(d, "fav_colors")
    {'blue', 'red', 'green'}
    >>> get_item(d, "fav_foods")
    {'pizza', 'ice cream', 'chocolate'}
    """
    return dictionary[key]


def get_item_from_user():
    """Given a dictionary and user input return the value for the key.
    >>> get_item_from_user()
    Enter a key: name
    d
    >>> get_item_from_user()
    Enter a key: age
    10
    >>> get_item_from_user()
    Enter a key: hobby
    programming
    >>> get_item_from_user()
    Enter a key: fav_nums
    [1, 2, 3]
    >>> get_item_from_user()
    Enter a key: fav_colors
    {'blue', 'red', 'green'}
    >>> get_item_from_user()
    Enter a key: fav_foods
    {'pizza', 'ice cream', 'chocolate'}
    """
    key = input("Enter a key: ")
    return get_item(d, key)


def get_all_keys(dictionary):
    """