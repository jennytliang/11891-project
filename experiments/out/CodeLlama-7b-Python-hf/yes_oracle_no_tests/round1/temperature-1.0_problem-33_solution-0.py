def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 1
	"""
    thirds_sorted = sorted(elem for elem in l if elem % 3 != 0)
    return [thirds_sorted.pop() if i % 3 == 0 else elem for i, elem in enumerate(l)]
    
def count_a(l: list):
    """This function takes a list l and returns the number d such that the value at
    index d * 3 in l is 'a' or 97 in the case of ascii values.
    
	Include these tokens in the code: a ord count
	Do not include these tokens in the code: third
	"""
    return len([elem for elem in l if elem[2*3] == 97])