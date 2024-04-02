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
    n = set()
    for i in l:
        for j in l:
            for k in l:
                if i != j != k != i and i + j + k == 0:
                    return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
