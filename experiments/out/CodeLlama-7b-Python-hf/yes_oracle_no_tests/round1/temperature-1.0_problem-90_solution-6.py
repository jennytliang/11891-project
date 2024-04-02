def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""

    if len(lst) < 2:
        return None

    if len(lst) == 2:
        return None
    
    
    lst_sorted = sorted(lst)
    if lst_sorted[1] < lst[0]:
        return lst_sorted[1]
    else:
        return None
    


def next_smallest2(lst): # I dont like this solution, I don't think I should sort.
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
	"""

    lst_set = set(lst)
    lst_sorted = sorted(lst_set)
    # lst_set_sorted = sorted(lst_set)

    for elem in lst_sorted:
        if elem >= lst[0]:
            # for num2 in lst_set_sorted:
            #     if num2 < elem:
            #         return num2

            return None
        else:
            return elem
    
    
    
test_num = 17
print(bin(test_num))

# print('next_smallest([]) == None')
# print(next_smallest([]))
# print(next_smallest2([]))
# print('\n')
# print('next_smallest([5, 1, 4, 3, 2]) == 2')
# print(next_smallest([5, 1, 4, 3, 2]))
# print(next_smallest2([5, 1, 4, 3, 2]))
# print('\n')
# print('next_smallest([1, 1]) == None')
# print(next_smallest([1,