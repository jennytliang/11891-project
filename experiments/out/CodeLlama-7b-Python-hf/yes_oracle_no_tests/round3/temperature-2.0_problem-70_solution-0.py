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
    pass


def first_plus_second_half(lst):
    '''
    Given list of integers, return first plus the sum of the rest of the numbers.
    Examples:
    first_plus_second_half([1, 2, 3, 4, 5]) == 9
    first_plus_second_half([1, 1, 1, 1, 1]) == 3
    first_plus_second_half([1, 2, 3]) == 6
    first_plus_second_half([1]) == 1
    first_plus_second_half([]) == 0
    
    Include these tokens in the code: sum _ list = sum ( lst )
    '''
    pass


def max_of_sublists(lst):
    '''
    Given list of integers, return list of maximum value of each sublist of 1 or more integers.
    Examples:
    max_of_sublists([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    max_of_sublists([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    max_of_sublists([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    max_of_sublists([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    max_of_sublists([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_of_sublists([1, 2, 3, 4, 5, 6, 7