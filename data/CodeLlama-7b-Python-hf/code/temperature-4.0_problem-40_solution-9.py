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
    """

    n = set()
    for i in l:
        n.add(-i)
    print(f"Unique numbers : {n = }")
    if n & set(l) == set():
        return

    n_ = set(map(lambda i:i*2, n))
    n_d = n.difference(l)
    for p in n_:
        for j in list(n_d):

            if -j==p and -j in l:
                # print(2*i, 2*j, -2*(p-j))
                return


    return False # no triple that can be formed with 0

l = range(14)
triples_sum_to_zero(l) # should return True. 12 is triple

if __name__