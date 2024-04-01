def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    result = []
    [result.append(a) for a in l if a > 0]
    return result    

def get_positive(l): 
    return [x for x in l if x > 0]
""""Return only positive numbers in a given list.
In this exercise you need to write less code -- the template has been 
written so it doesn't need much edits. The solution could not be made shorter than 
10 lines. The only requirement is that use the template to return only the positive numbers from the list of numbers. 
Do not use the sum method or any list method. Try to accomplish this in a single for loop (hint: there can be several on a single loop). 
The order of the input and output array do not matter."""               