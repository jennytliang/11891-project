def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Do not include these tokens in the code: def get _ min ( lst ):
	'''
    if len(lst) < 2:
        return lst
    lst = lst[:]
    lst.sort()
    result = []
    while len(lst) > 1:
        result.append(lst[0])
        lst = lst[1:]
        lst.sort()
    result.append(lst[0])
    return result



print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
print(strange_sort_list([6, 2, 3, 4, 5]))
print(strange_sort_list([1, 4, 3, 2, 5]))
print(strange_sort_list([5, 4, 3, 2, 1]))
print(strange_sort_list([1, 2, 3, 4, 5, 6]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11