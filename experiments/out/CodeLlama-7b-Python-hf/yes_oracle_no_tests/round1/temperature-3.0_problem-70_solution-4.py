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
    def get_min(lst):
        min_value = lst[0]
        for i in lst:
            if i < min_value:
                min_value = i
        return min_value
    def get_max(lst):
        max_value = lst[0]
        for i in lst:
            if i > max_value:
                max_value = i
        return max_value
    def get_sorted_list(lst):
        sorted_list = []
        while lst != []:
            sorted_list.append(get_min(lst))
            lst.remove(get_min(lst))
            sorted_list.append(get_max(lst))
            lst.remove(get_max(lst))
        return sorted_list
    return get_sorted_list(lst)














