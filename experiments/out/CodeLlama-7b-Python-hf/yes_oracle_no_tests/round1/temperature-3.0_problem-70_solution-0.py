def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list
	Do not include these tokens in the code: if lst == [] :
	'''
    sorted_list = sorted(lst)
    strange_list = []
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            strange_list.append(sorted_list[0])
            sorted_list.pop(0)
        else:
            strange_list.append(sorted_list[-1])
            sorted_list.pop(-1)
    return strange_list


#print(strange_sort_list([1, 2, 3, 4]))
#print(strange_sort_list([5, 5, 5, 5]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#print(strange_sort_list([5, 4, 3, 2, 1, 6]))
#print(strange_sort_list([]))
#print(strange_sort_list([1]))
#print(strange_sort_list([1, 1]))
#print(strange_sort_list([1, 2]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
