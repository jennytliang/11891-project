def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: ans , i , j = [], 0
	'''


    sorted_list = sorted(lst)
    ans = []
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            ans.append(sorted_list[0])
            sorted_list.remove(sorted_list[0])
        else:
            ans.append(sorted_list[-1])
            sorted_list.remove(sorted_list[-1])
    return ans
























































