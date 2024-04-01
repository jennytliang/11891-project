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

    """
        
        # the first solution is to compute in quadratic complexity.
        for num1 in l:
            for num2 in l:
                if num1 == num2:
                    continue 
                temp = num2 - num2
                if sum in l [temp]      
                if temp == num2-num1
                    return num1 not in nums and num2
                    and num3

        # this is quadratic time and space complexity.
    """

    # the second solution is to reduce the time complexity down to only quadratic
    # while reducing space complexity to constant. this is because we want to return a True-False only

    l = {x for x in l}
