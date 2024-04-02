def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: list
	Do not include these tokens in the code: lst
	'''

    
 
    # write your code here
    if len(lst) == 0:
        return []
    else:
        min = lst[0]
        max = lst[0]
        for i in lst:
            if i < min:
                min = i
            if i > max:
                max = i
        lst.remove(min)
        lst.remove(max)
        return [min, max] + strange_sort_list(lst)
    

    # another solution
    #if lst == []:
    #    return []
    #else:
    #    return [min(lst)] + max(lst) + strange_sort_list(lst)


def strange_sort_list_2(lst):
    if len(lst) < 2:
        return lst
    return [min(lst)] + max(lst) + strange_sort_list_2(lst)


#print(strange_sort_list([1, 2, 3, 4]))
#print(strange_sort_list([5, 5, 5, 5]))
#print(strange_sort_list([]))
print(strange_sort_list_2([1, 2, 3, 4]))
print(strange_sort_list_2([5, 5, 5, 5]))
print(strange_sort_list_2([]))
