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
        fo = []
        for j in range(len(l)):
            if i == j:
                continue
            for k in range(len(l)):
                if k == i or k == j:
                    continue
                if l[i] + l[j] + l[k] == 0:
                    fo.append(l[i])
                    fo.append(l[j])
                    fo.append(l[k])
                    return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()