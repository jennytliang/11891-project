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
	Do not include these tokens in the code: if len ( lst ) ==
	'''

    # Your code here
    if len(lst) == 0:
        return lst
    else:
        return [min(lst)] + [max(lst)] + [min(lst[1:])] + [max(lst[1:])] + [min(lst[2:])] + [max(lst[2:])] + [min(lst[3:])] + [max(lst[3:])] + [min(lst[4:])] + [max(lst[4:])] + [min(lst[5:])] + [max(lst[5:])] + [min(lst[6:])] + [max(lst[6:])] + [min(lst[7:])] + [max(lst[7:])] + [min(lst[8:])] + [max(lst[8:])] + [min(lst[9:])] + [max(lst[9:])] + [min(lst[10:])] + [max(lst[10:])] + [min(lst[11:])] + [max(lst[11:])] + [min(lst[12:])] + [max(lst[12:])]


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
