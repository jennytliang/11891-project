def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( max _ element ([ 1 ,
	"""


    return maax(l, 0, len(l) - 1)

def maax(l, left, right):
    if left == right:
        return l[left]
    mid = (left + right) // 2
    m1 = maax(l, left, mid)
    m2 = maax(l, mid + 1, right)
    if m1 > m2:
        return m1
    return m2



def max_element1(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """


    return maax1(l, 0, len(l) - 1)

def maax1(l, left, right):
    if left == right:
        return l[left]
    mid = (left + right) // 2
    m1 = maax1(l, left, mid)
    m2 = maax1(l, mid + 1, right)
    if m1 > m2:
        return m1
    return m2



def max_element2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """


    return maax2(l, 0, len(l) - 1)

def maax2(l, left, right):
    if left == right:
        return l[left]
    mid = (left + right) // 2
    m1 = maax2(l, left, mid)
    m2 = maax2(l, mid + 1, right)
    if m1 >