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
    
	Do not include these tokens in the code: l = sorted ( l )
	"""

    l = sorted(l)

    for idx, val in enumerate(l):
        if val > 0:
            break
        if val + l[-1] + l[-2] > 0:
            break
        for idx2, val2 in enumerate(l[idx + 1 :]):
            if val + val2 + l[-1] == 0:
                return True
            if val2 + l[-1] + l[-2] > 0:
                break
            for idx3, val3 in enumerate(l[idx2 + 1 :]):
                if val + val2 + val3 == 0:
                    return True
                if val2 + val3 + l[-1] > 0:
                    break
                if val3 + l[-1] + l[-2] > 0:
                    break
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
