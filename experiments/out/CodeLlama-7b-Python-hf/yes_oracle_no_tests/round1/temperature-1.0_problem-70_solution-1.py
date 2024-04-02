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
    # Your code here
    if len(lst) == 0:
        return []
    else:
        sorted_list = sorted(lst)
        result = [sorted_list[0]]
        for i in range(1, len(sorted_list)):
            result.append(sorted_list[-i])
            result.append(sorted_list[i])
        return result


# Solution 2
# def strange_sort_list(lst):
#     if len(lst) < 2:
#         return lst
#     else:
#         return [lst[0]] + strange_sort_list(lst[1:]) + [lst[0]]
