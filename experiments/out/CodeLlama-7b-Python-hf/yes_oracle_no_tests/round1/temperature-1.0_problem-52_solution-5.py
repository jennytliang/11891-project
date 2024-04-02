def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    return all(x < t for x in l)
    
def same_shape(m1, m2):
    """
    Return True if m1 and m2 have the same shape.
    Assume that m1 and m2 only have Nones at the edge.

    >>> same_shape([[1, 2, 3], [4, 5, None]], [[1, 2, 3], [4, None, 5]])
    True
    >>> same_shape([[1, [2]], None, 3, [4, [5]]], [[1, [2]], [None], 3, [4, [5]]])
    True
    """
    if m1 == [] or m2 == []:
        return True
    else:
        # if both are Nones, then return true
        if (m1[0] == None) == (m2[0] == None) and (m1[1] == None) == (m2[1] == None):
            return True
        # if one or both aren't, then both must not be Nones and then they should be equal
        elif not((m1[0] == None) == (m2[0] == None)) or not((m1[1] == None) == (m2[1] == None)):
            return m1[0] == m2[0] and m1[1] == m2[1] and same_shape(m1[1], m2[1])
            
def is_right(t1: list, t2: list):
    """Return True if either of the trees rooted at t1 and t2 is a full tree with right
    skew and the other is a perfect tree and is to the right of the first, False otherwise.

    Preconditions: both t1 and t2 are full, with right skew in t1
    (i.e. their subtrees must all have right skew).

    >>> is_right([1, [2, None]],
    ...         [[1, [[None, 2], None]]]) <==>
    >>> is_right(binary_tree(1, binary_tree(