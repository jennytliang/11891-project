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
    lst = sorted(lst)
    while len(lst) > 0:
        min_value = lst[0]
        lst.remove(min_value)
        lst.insert(0, min_value)
        lst.append(min_value)
        lst.remove(min_value)
        lst.sort()
    return lst


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "1st example"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "2nd example"
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], "3rd example"
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Reverse example"
    assert strange_sort_list([1, 2, 3, 5, 4, 6, 8, 7]) == [1, 8, 2, 7, 3, 6, 4, 5], "Not sorted example"
    assert strange_sort_list([99, 77, 44, 31, 10, 20]) == [10, 20, 31, 44, 77, 99], "Not sorted 2 example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
