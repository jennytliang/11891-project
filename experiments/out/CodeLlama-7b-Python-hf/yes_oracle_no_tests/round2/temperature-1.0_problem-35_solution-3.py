def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print (" Example : ") print ( max
	"""


    return maax(l, 0)


# Helper recursive function does most of the work
def maax(l: list, max_element):
    # base cases for recursion
    if len(l) == 1:  # list of size 1 has one maximum element, so we return it
        return l[0]
    elif len(l) == 0:  # list of size 0 has no elements, so we return what we were given as the initial max
        return max_element

    # first element of list is greater
    elif l[0] > l[1]:
        return maax(l[1:], l[0])

    # second element of list is greater
    return maax(l[1:], l[1])


# This is provided for your convenience as a wrapper to
# call the recursive implementation of your choice


def recursive_max_element(l: list):
    return max_element(l)