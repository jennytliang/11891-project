def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    
	Do not include these tokens in the code: n = set ()
	"""

    # add code here
    from collections import defaultdict
    d = defaultdict(int)
    for i in l:
        d[i] += 1
        if i == 0 and d[i] > 2:
            return True
        elif d[i] > 1:
            if -i in d:
                return True
    return False


# print(triples_sum_to_zero([1, 3, -2, 1]))
