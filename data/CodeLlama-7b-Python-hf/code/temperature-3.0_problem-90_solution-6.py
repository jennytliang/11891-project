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

    def check_small(lst, element):
        lst = lst[element + 1:]
        for i in lst:
            if i <= element:
                return False
        return True

    if lst == []:
        return None

    smallest = min(lst)
    for i in lst:
        if i > smallest and i < lst[-1]:
            return i

    lst = lst[::-1]
    for i in lst:
        if i < smallest:
            return i

    return None
