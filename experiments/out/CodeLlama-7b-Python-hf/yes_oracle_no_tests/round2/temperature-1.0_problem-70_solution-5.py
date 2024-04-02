def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    
    # Your code here
    if not lst:
        return []
    
    lst = sorted(lst)
    lst = lst[0:1] + lst[-1:] + lst[1:-1]
    return lst


def strange_sort_dict(dct):
    '''
    Given dictionary, return dictionary in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_dict({1: 1, 2: 2, 3: 3, 4: 4}) == {1: 1, 4: 4, 2: 2, 3: 3}
    strange_sort_dict({5: 5, 5: 5, 5: 5, 5: 5}) == {5: 5, 5: 5, 5: 5, 5: 5}
    strange_sort_dict({}) == {}
    
	Include these tokens in the code: sorted _ dict =
	Do not include these tokens in the code: return
	'''
    # Your code here
    if not dct:
        return {}
    
    lst = sorted(dct.values())
    lst = lst[0:1] + lst[-1:] + lst[1:-1]
    return dict(zip(lst, dct.keys()))