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
    mini = None

    # check that it's of at least two length so that there is another element
    if (len(lst) >= 2 and
            lst[1:] != 
                sorted(lst[1:])): # check for ordered
    # iterate through each element and check that the index of this element is greater than the previous element.  Set the minium as the first found minimum.  if not found then return min.
        # mini = mini or 0
        mini = lst[0]
        for idx, element in enumerate(lst[1:]):   # ignore first in list, so slice
            if idx+mini < element:
                mini = idx
                break
   
    return mini    
      

    
                      

