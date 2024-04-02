def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    new_list = []
    even_numbers = []
    even_numbers.append(l[0])
    for i in l[1:]:
        if i % 2 == 0:
            return None
        else:
            new_list.append(i)
    new_list = sorted(new_list)
    even_numbers = even_numbers + new_list
    return even_numbers

def sort_even2(l):
    """
	Another implementation
	"""
    return l[::2] + sorted(l[1::2])

print(sort_even2([5, 6, 3, 4]))    