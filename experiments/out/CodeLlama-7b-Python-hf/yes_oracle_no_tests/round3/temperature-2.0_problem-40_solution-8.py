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
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    for i in range(len(l)):
        fo = l[i]
        for j in range(i+1, len(l)):
            sec = l[j]
            for k in range(j+1, len(l)):
                thi = l[k]
                if (fo + sec + thi) == 0:
                    return True
    return False


print(triples_sum_to_zero([1, 3, -2, 1]))
