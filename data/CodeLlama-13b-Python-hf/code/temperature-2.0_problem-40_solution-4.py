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
    # if len(l) < 3:
    #     return False
    # for i in range(len(l) - 2):
    #     for j in range(i + 1, len(l) - 1):
    #         for k in range(j + 1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False

    # l.sort()
    # for i in range(len(l) - 2):
    #     if l[i] > 0:
    #         return False
    #     left = i + 1
    #     right = len(l) - 1
    #     while left < right:
    #         if l[left] + l[right] + l[i] == 0:
    #             return True
    #         elif l[left] + l[right] + l[i] < 0:
    #             left += 1
    #         else:
    #             right -= 1
    # return False

    l.sort()
    for i in range(len(l) - 2):
        if l[i] > 0:
            return False
        if i > 0 and l[i] == l[i - 1]:
            continue
        left = i + 1
        right = len(l) - 1
        while left < right:
            if l[left] + l[right] + l[i] == 0:
                return True
            elif l[left] + l[right] + l[i] < 0:
                left += 1
            else:
                right -= 1
    return False



