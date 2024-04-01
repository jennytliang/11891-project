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

    if len(lst)  < 2:
        return None

    lst.sort()
    for i in range(len(lst)):
        if lst[i] < lst[i+1]:
            return lst[i+1]

    return None
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert next_smallest([1, 2, 3, 4, 5]) == 2, "Example"
    assert next_smallest([5, 3, 2, 1, 0]) == None, "Only zeros"
    assert next_smallest([2, 2, 1, 0, 0]) == 1, "Only same numbers"
    assert next_smallest([-3, 100, 9, 1]) == 9, "Negatives"
