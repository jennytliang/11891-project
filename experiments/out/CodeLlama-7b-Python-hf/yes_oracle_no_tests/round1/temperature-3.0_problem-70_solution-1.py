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
    lst = sorted(lst)
    result = []
    while lst:
        result.append(min(lst))
        lst.remove(min(lst))
        result.append(max(lst))
        lst.remove(max(lst))
    return result


if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))
    print(strange_sort_list([5, 5, 5, 5]))
    print(strange_sort_list([]))
