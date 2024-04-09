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
    
	Do not include these tokens in the code: if len ( l ) <
	"""
    # your code here
    for first in l:
        for second in l:
            if first == second:
                continue
            for third in l:
                if first == third or second == third:
                    continue
                if first + second + third == 0:
                    return True
    return False


print(triples_sum_to_zero([1, 2, 3, 7]))
