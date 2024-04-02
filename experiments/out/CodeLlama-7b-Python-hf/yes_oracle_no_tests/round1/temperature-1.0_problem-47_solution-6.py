def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    m = len(l) // 2
    # BEGIN PROBLEM 1
    lc = l[:m]
    lc += [l[-1]]
    rc = [-float('inf')]
    rc += l[m:]
    rc += [float('inf')]
    
    return (lc[lc.index(sorted(lc)[m-1])] + \
                     rc[rc.index((s)orted(rc)[m])]) / 2
    # END PROBLEM 1

        

def bisection_search(elem, alist, lower_index=0, upper_index=None):
    """Returns index of elem if elem is in alist, else None.
    Return value is a potentially incorrect index, but this should not
    matter for application of this function as long as the index is not out of
    bounds for alist.
    
    If it matters that the alist is sorted, pass True for the last parameter.
    The runtime will then be O(log n) due to bisect, but it's only slightly more
    efficient than O(n) O(log n) because it's easier to implement.
    
    >>> bisection_search(3,[1,2,3]) # Returns 2, not -1, because index 2 is 3
    2
    >>> bisection_search(18,[1,2,3])
    >>> bisection_search(3,[-10,2,3,15,18,20])
    """
    if upper_index is None:
        upper_index = len(alist)
    mid = (lower_index + upper_index) // 2 # midpoint
    if alist[mid] == elem:
        return mid
    elif lower_index == upper_index:
        return None
    elif (lower_index < upper_index and elem < alist[mid]):
        return bisection_search(elem, alist, lower_index, mid)
    elif lower_index < upper_index and elem >= alist[mid]:
        return bisection_