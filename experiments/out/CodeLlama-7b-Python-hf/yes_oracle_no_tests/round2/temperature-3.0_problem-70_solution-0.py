def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: ans , i , j
	Do not include these tokens in the code: strange _ list
	'''

    sorted_list = sorted(lst)

    ans = []
    for i in range(len(lst)):
        if i % 2 == 0:
            ans.append(sorted_list.pop(0))
        else:
            ans.append(sorted_list.pop(-1))

    return ans


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
