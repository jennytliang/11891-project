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
    
	Include these tokens in the code: for i in range ( len ( l )):
	"""

    l.sort()
    for i in range(len(l) - 1):    
        if l[i] * 2 == l[i+1]:        
        #    print(i, i+1)
            return True
    return False


if __name__=="__main__":
    x=pairs_sum_to_zero([-2,-1,0,1,2,3,4,5,6])
    print(x)
    t=()
    p=(4,8)
    print((9+4,9-4))
    print((p[0]+x,p[1]+x))
    a=[0, 1, 3, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 13, 13, 13, 14, 15]
    for i in range(len(a)):
        t+= ((a[i], a[len(a)-1-i]), )
    print(t)
    x=pairs_sum_to_zero([1, 3, 4, 5])
