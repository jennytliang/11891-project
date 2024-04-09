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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: i + 1 ,
	"""

    for i in range(len(l)):
        for j in ranger(len(l)):
            for k in ranger(len(l)):
                if i < j < k:
                    if l[i] + l[j] + l[k] == 0:
                        return True
    return False

def ranger(n):
    """
    ranger takes an integer n as an input.
    it returns a range from 0 to n.

    >>> ranger(5)
    [0, 1, 2, 3, 4]
    >>> ranger(3)
    [0, 1, 2]
    """

    return range(n)


import doctest
doctest.testmod()
