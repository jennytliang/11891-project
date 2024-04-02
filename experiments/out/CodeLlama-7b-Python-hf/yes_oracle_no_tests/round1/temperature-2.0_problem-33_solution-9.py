def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third = [ l [ i ] for i in
	"""
    # write your code here
    third = [l[i] for i in range(len(l)) if i % 3 != 0]
    third_sorted = sorted(third)
    return [third_sorted[i] if i % 3 == 0 else l[i] for i in range(len(l))]


def sort_third_v2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third = [ l [ i ] for i in
	"""
    # write your code here
    return [l[i] if i % 3 == 0 else sorted(l)[i] for i in range(len(l))]


# print(sort_third([1, 2, 3]))
# print(sort_third([5, 6, 3, 4, 8, 9, 2]))

print(sort_third_v2([1, 2, 3]))
print(sort_third_v2([5, 6, 3, 4, 8, 9, 2]))
