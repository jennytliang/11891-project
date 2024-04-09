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
	Do not include these tokens in the code: # Your code here if
	'''
    lst = sorted(lst)
    i = 0
    while i < len(lst):
        if i == len(lst)-1:
            lst.append(lst[i])
            break
        else:
            lst.append(lst[i])
            i += 2
    return lst


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "1st example"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "2nd example"
    assert strange_sort_list([1, 2, 3]) == [1, 3, 2], "3rd example"
    assert strange_sort_list([]) == [], "Empty"
    assert strange_sort_list([1, 1, 1, 2, 2, 2]) == [1, 2, 1, 2, 1, 2], "Repeated"
