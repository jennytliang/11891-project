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
	Do not include these tokens in the code: # sort the lst
	'''
    # YOUR CODE HERE
    count = 1
    sorted_lst = sorted(lst)
    length = len(sorted_lst) - 1
    for _ in range(len(lst)):
        print(sorted_lst[0])
        lst.remove(sorted_lst[0])
        sorted_lst.remove(sorted_lst[length])
        print(sorted_lst[length])
        count += 1
        length -= 1
    return lst


#simple_sorting = [[2], [3], [4]]
#print(simple_sorting)

simple_sorting = [
    ("I",2),
    ("am",3),
    ("leet",4),
]

print(strange_sort_list(simple_sorting))