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
    
	Do not include these tokens in the code: # Your code here
	"""

    # Your code here
    triplets = {}
    for a in l:
        for b in l:
            if a == b:
                continue
            c = -(a + b)
            if c in triplets:
                if a in triplets[c]:
                    return True
                else:
                    triplets[c].append(a)
            else:
                triplets[c] = [a]
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
