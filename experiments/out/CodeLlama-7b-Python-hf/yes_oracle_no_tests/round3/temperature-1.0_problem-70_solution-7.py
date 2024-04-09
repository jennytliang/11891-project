def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: # Your code here
	'''
    # Your code here
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        min = lst[0]
        max = lst[-1]
        lst = [x for x in lst if x != min and x != max]
        lst.append(min)
        lst.append(max)
        return lst


print(strange_sort_list([2, 1, 5, 3, 4, 7]))
print(strange_sort_list([2, 1, 5, 3, 4]))
print(strange_sort_list([2, 1, 5, 3]))
print(strange_sort_list([2, 1, 5]))
print(strange_sort_list([2, 1]))
print(strange_sort_list([2]))
print(strange_sort_list([]))
