def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''
    return sorted(lst)

def strange_sort_dict(dct):
    '''
    Given dictionary, return dictionary in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_dict({1:1, 2:2, 3:3, 4:4}) == {1:1, 4:4, 2:2, 3:3}
    strange_sort_dict({5:5, 5:5, 5:5, 5:5}) == {5:5, 5:5, 5:5, 5:5}
    strange_sort_dict({}) == {}
    
	Include these tokens in the code: sorted _ dct = sorted ( dct )
    '''
    return sorted(dct)

def strange_sort_tuple(tup):
    '''
    Given tuple, return tuple in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_tuple((1, 2, 3, 4)) == (1, 4, 2, 3)
    strange_sort_tuple((5, 5, 5, 5)) == (5, 5, 5, 5)
    strange_sort_tuple(()) == ()
    
	Include these tokens in the code: sorted _ tup = sorted ( tup )
    '''
    return sorted(tup)
