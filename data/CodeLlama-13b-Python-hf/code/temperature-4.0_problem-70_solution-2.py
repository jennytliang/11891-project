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
    # return the sorted list

    # find max
    lst_min=[]
    for _ in range(len(lst)):
        min_value= min(lst)
        lst_min.append(min_value)
        lst.remove(min_value)
    lst +=lst_min

    #return  reverse sorted lst
    lst_rev=(lst).sort(reverse=True),
    return lst(lst_rev) 
    
# lst= [1, 2, 3, 4,]
# print (strange_sort(lst))


    