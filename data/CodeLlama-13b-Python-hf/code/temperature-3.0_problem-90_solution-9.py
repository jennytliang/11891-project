def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # 1st approach
    # n = lst[:]
    # lst2 = n[1:]
    # n.remove(min(n))
    # lst2.remove(min(lst2))
    # lst.sort()
    # if lst2 == []:
    #     return 'None'
    
    # return lst2[0]
    
    # 2nd approach
    
    nums = lst[:]
    lst2 = nums[1:]
    nums.remove(min(lst))
    lst2.remove(min(lst2))
    lst.sort()
    if lst2 == []:
        return 'None'
    
    return lst2