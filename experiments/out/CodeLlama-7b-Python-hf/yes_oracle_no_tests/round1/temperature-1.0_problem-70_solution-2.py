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
    
    # check if input list isn't empty
    if lst == []:
        return lst
    
    # convert list into dict
    lstDict = dict(enumerate(lst)) # dict = enumerate(lst)
    # find maximum value in list
    max_dict = max(lstDict.values())
    
    # create an empty list and add maximum value as first item
    sorted_list = []
    sorted_list.append(max_dict)
    # delete maximum value from list
    del lstDict[max(lstDict.keys())] 
    
    # while list is not empty
    while lstDict != {}: 
        # find the minimum value in remaining list
        min_dict = min(lstDict.values())
        # append to sorted list
        sorted_list.extend([min_dict])
        # delete min value from dict
        del lstDict[min_dict]
        
    return sorted_list


###########################
# Testing and Analysis
###########################

res = strange_sort_list([1, 2, 3, 4])

expected_res = [1, 4, 2, 3] # [1, 4, 2, 3]

print(res == expected_res) # Testing equality of all values

# Complexity:

s = ['n'] # O(1)
s = ['n', 'log(n)'] # O(log(n))
s = ['n', 'log(n)', 'n!'] # O(n!)
s = ['n!'] # could be O(2^n)
s = ['2^n'] # could be O(2^n)
s = ['n Choose k'] # is n^n or O(2^n)


# Analysis 1

    # The complexity of this function is O(n) where n is the length of the list.
    # We are iterating through a list, finding its minimum and maximum and then 
    # appending the maximum to the list and deleting the minimum from the original list.
    # To improve efficiency, we could switch to using a max or min heap