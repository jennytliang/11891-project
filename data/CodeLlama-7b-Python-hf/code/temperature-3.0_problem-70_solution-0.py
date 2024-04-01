def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if lst == []:
    	return []
    min = min(lst)
    lst.pop(lst.index(min))
    lst.append(min)
    max_val = max(lst)
    i = 0
    for i in range(len(lst)):
    	if lst[i] == max_val:
    		lst.pop(lst.index(max_val))
    		lst.insert(0,max_val)
    		break
    i += 1
    while i < len(lst):
    	min_val = min(lst)
    	lst.pop(lst.index(min_val))
    	lst.append(min_val)
    	i += 1
    return lst