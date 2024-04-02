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
        for j in rangle(i, len(l) - 1):
            if (l[j] + l[i] == 0 and l[i] != 0 and l[j] != 0):
                print("Sum :  " + str(l[j]+l[i]))
                return True
    return False


# The following lines need to be included if you do not define the variable above

triples_sum_to_zero([1, 3, -2, 1])
triples_sum_to_zero([1, 3, -2, 0])
triples_sum_to_zero([2, 4, -5, 3, 9, 7])
triples_sum_to_zero([1, 2, 3, 7])
triples_sum_to_zero([1])
