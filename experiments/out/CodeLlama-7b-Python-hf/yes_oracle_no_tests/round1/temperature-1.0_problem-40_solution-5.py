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
        for j in r
    
    n1 = l[i]
    n2 = l[(i + 1) % len(l)]
    n3 = l[(i + 2) % len(l)]

# Solution --------------------------------------------------
    if len(numbers) < 3: return False

    n1, n2, n3 = numbers[0:3]
    assert n1 != n2
    assert n2 != n3

    if (n1 + n2 + n3) == 0:
        return True
    elif len(numbers) < 3:
        return False
    return triples_sum_to_zero(numbers[1:])

print(triples_sum_to_zero([0,0,0]))
