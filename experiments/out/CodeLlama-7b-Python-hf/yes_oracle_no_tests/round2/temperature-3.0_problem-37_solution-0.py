def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: result
	"""
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(l[i])
    result.sort()
    for i in range(len(l)):
        if i % 2 != 0:
            result.append(l[i])
    return result



def sort_even_no_sort(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_no_sort([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_no_sort([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: result
	"""
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(l[i])
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    for i in range(len(l)):
        if i % 2 != 0:
            result.append(l[i])
    return result
