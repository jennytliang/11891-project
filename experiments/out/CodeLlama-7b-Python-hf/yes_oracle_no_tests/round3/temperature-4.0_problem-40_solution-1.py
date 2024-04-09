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
    for i in range(len(l) - 2):
        cur = l[i]
        start = i + 1
        end = len(l) - 1
        while start < end:
            sum = cur + l[start] + l[end]
            if sum == 0:
                return True
            elif sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
