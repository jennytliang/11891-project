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
    """
    # for i in l: # for every number i in the list l...
    #     for e in l[ l.index(i)+1 : ]: if i+e is 0 return True. # loop over all items in the list l from i to its end...  if there is any item e in the list... which makes item i and e equal 0 (additive inverse of item i) then...
