def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: def pairs _ sum _ to
	"""

    # add your code here
    result_boolean = False
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == 0:
                return result_boolean
    return result_boolean

    
def pairs_sum_to_zero_v2(l):
    # another way to do it, I'm too much old school
    set_l = set(l)
    for x in set_l:
        if -x in set_l and l.count(x) > 1 and -x != x:
            return True # I should have just returned x,y tuples, but oh well.
    else: # we never found a pair that summed to 0, oh well.
        return False

def pairs_sum_to_zero_v3(l):
    set_l = set(l)
    return any( (i, -i) in set_l**2 for i in set_l if (-i in set_l))


# Test code, just ignore.
import doctest
doctest.testmod()
