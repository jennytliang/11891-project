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
    # your code here
    lst = sorted(lst)
    return [lst[0]] + [lst[-1]] + lst[1:-1]


def check(candidate):

    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [
        1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [
        1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 7, 6]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [
        1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 8, 7, 6]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [
        1, 14, 2, 