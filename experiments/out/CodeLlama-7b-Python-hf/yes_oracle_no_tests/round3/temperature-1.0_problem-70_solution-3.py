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
    return sorted ( lst )


if __name__ == '__main__':
    print("Example:")
    print(strange_sort_list([1, 2, 3, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([1, 3, 5, 7]) == [1, 7, 3, 5]
    print("Coding complete? Click 'Check' to earn cool rewards!")