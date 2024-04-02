def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Do not include these tokens in the code: Rec ursive Solution
	'''
    strnge_list = []
    
    if lst:
        minval = min(lst)
        maxval = max(lst)
        
        strnge_list.append(minval)
        strnge_list.append(maxval)
        strnge_list.extend(strnge_list + lst)
        strnge_list.pop()

        return strnge_list
    else:
        return []

    #if __name__ == '__main__':
    #    print(strange_sort_list([7, 2, 9, 5, 1]))