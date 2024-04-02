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
    
	Include these tokens in the code: range ( len ( l )):
	Do not include these tokens in the code: :
	"""


    foos = []
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                for k in range(len(l)):
                    if i != k and j != k:
                        if l[i] + l[j] + l[k] == 0:
                            foos.append([l[i], l[j], l[k]])

    if len(foos) > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
