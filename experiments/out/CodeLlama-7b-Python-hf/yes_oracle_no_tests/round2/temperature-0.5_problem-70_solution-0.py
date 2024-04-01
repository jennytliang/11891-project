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
    lst = sorted(lst)
    result = []
    while len(lst) > 0:
        result.append(lst[0])
        lst.remove(lst[0])
        result.append(lst[-1])
        lst.remove(lst[-1])
    return result


if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))
    print(strange_sort_list([5, 5, 5, 5]))
    print(strange_sort_list([]))
