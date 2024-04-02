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

    if len(lst) <= 1:
        return None

    # Set the smallest item to the first item
    smallest = lst[0]

    # Iterate through the list
    for i in range(len(lst)):

        # If the current item is smaller than the smallest item, set it to the smallest item
        if lst[i] <= smallest:
            smallest = lst[i]

    # Create the new list
    new_lst = []

    # Iterate through the list and append items that are greater than the smallest item
    for i in range(len(lst)):
        if lst[i] > smallest:
            new_lst.append(lst[i])

    # If the new list is empty, return None
    if len(new_lst) == 0:
        return None

    # Sort the new list
    new_lst.sort()

    # Return the first item in the new list
    return new_lst[0]
