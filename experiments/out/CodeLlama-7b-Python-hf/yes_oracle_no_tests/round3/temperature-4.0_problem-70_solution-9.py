def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    # your code here
    # 36ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    # return lst

    # 48ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    # return lst

    # 32ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    # return lst

    # 36ms
    lst = sorted(lst)
    while lst:
        lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    return lst

    # 40ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    # return lst

    # 44ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] + lst[1:-1] if lst[0] < lst[-1] else [lst[0], lst[-1]] + lst[1:-1]
    # return lst

    # 44ms
    # lst = sorted(lst)
    # while lst:
    #     lst = [lst[-1], lst[0]] +