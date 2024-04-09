def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: def min _ element ( l : list ):
	"""

    
    returnt = l[0]
    for i in l:
        if i > returnt:
            returnt = i
    return returnt


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: def min _ element ( l : list ):
	"""


def first_occurence(l: list, e: object):
    """Return index of first occurrence of e in l.
    >>> first_occurence([1, 2, 3, 2, 3], 2)
    1
    >>> first_occurence([1, 2, 3, 2, 3], 3)
    2
    
	Do not include these tokens in the code: def first _ occurence ( l : list, e : object ):
	"""


def last_occurence(l: list, e: object):
    """Return index of last occurrence of e in l.
    >>> last_occurence([1, 2, 3, 2, 3], 2)
    4
    >>> last_occurence([1, 2, 3, 2, 3], 3)
    5
    
	Do not include these tokens in the code: def last _ occurence ( l : list, e : object ):
	"""


def index(l: list, e: object):
    """Return index of first occurrence of e in l.
    >>> index([1, 2, 3, 2, 3], 2)
    1
    >>> index([1, 2, 3, 2, 3], 3)
    2
    
	Do not include these tokens in the code: def index ( l : list, e : object ):
	"""


