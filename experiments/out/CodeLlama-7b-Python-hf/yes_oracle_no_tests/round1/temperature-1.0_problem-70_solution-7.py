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
    # sort the list
    lst = sorted(lst)
    
    # use a while loop with two variables:
    # 1. index to keep track of the maximum value
    # 2. length to keep track of the number of elements to return from the list
    i = 0
    length = len(lst)
    result = []
    while length != 0:
    # loop through the list and alternate the min and max values, based on the length
    
        # set j and length equal to the length
        j = length
        length = length // 2
        # set the max_length equal to the length
        max_length = length
        # set current_length = max_length
        current_length = max_length
        # decrease max_length by 1
        max_length -= 1
        # while current_length >= 0
        while current_length >= 0:
        # the inner while loop is used to loop through the list once, until we reach a point where there are no more elements left in the list to work with
            
            # if j is less than or equal to the length
            if j <= length:
            # if lst[j] is less than or equal to the lst[index]
                if lst[j] <= lst[i]:
                # append lst[j] to the result
                    result.append(lst[j])
                # set j equal to j + max_length
                    j += max_length
            # otherwise, j is greater than the length
            else:
                # append lst[index] to the result
                    result.append(lst[i])
                # increase i by 1
                    i += 1
        # subtract length from j
            j -= length
        # subtract length from the current length
        # set current length to the new current length
        current_length -= length
    # return the result
    return result