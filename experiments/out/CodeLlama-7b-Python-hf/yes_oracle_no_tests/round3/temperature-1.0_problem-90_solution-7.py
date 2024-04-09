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

    
    i = 0
    smallest = None
    while i < len(lst):
        if smallest == None:
            smallest = lst[i]
        elif lst[i] <= smallest:
            smallest = lst[i]
        i += 1
    
    i = 0
    second_smallest = None
    while i < len(lst):
        if second_smallest == None:
            second_smallest = lst[i]
        elif lst[i] <= second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
        i += 1
        
    if second_smallest != None:
        return second_smallest
    else:
        return None
    
    #return second_smallest


if __name__ == '__main__':
    print(next_smallest([1, 2, 3, 4, 5]))
    # 2
    
    print(next_smallest([5, 1, 4, 3, 2]))
    # 2
    
    print(next_smallest([]))
    # None
    
    print(next_smallest([1, 1]))
    # None