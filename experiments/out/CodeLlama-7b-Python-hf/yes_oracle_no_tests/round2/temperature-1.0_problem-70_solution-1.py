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
	Do not include these tokens in the code: result
	'''
    odd = list(filter(lambda x: x%2 == 1, lst))
    even = list(filter(lambda x: x%2 == 0, lst))
    new_lst = sorted(odd + even)
    
    return new_lst

 

if __name__ == '__main__':
    print("Example:")
    print(strange_sort_list([1, 2, 3, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([0]) == [0]
    assert strange_sort_list([]) == []
    assert strange_sort_list([10, 80, 100, 101, 2]) == [2, 100, 80, 101, 10]
    print("Coding complete? Click 'Check' to earn cool rewards!")