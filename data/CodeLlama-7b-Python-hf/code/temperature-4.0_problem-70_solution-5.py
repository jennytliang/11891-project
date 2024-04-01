def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    return sorted(lst, key=lst.count)
    
    # alternate:

def weird_order(in_list):
    """Weird sort from left to right: first, all the min's; then, all
    max's; and then, all min's again.
    For example:
    [3, 4, 5, 8, -2, -5, -10, -1] == [-10, -5, -1, -2]
    [3, 3, 2, 2, 1, 5, 5] == [1, 2, 2, 3, 3]
    [2, -4, -2, 10, -5] == [-5, -4]
    [] == []
    
    >>> weird_order([3, 4, 5, 8, -2, -5, -10, -1])
    [-10, -5, -1, -2]
    >>>

if __name__=="__main__":
    n = input_list()
    print_output(odd_sort_filter(n))
     
