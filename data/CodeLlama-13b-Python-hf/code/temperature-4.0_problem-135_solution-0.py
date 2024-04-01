def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # sort and add the list elements together, then sort again and compare each 1'st in pair with the previous value:
    return max((max(sorted(_) + sorted(_, key=lambda n: -n)[1:]) +
               max(sorted(_[::-1]+ _[:-1])[::-1]))/2 for _ in (zip([arr[i], arr[i-1]] 
               for i in range(len(arr[:-1]))) )) -1
        
      
    
if __name__ == '__main__':
    assert can_arrange([1,2,4,3,5,6,-6]) == 3
    # can_arrange([1, 3, 2, 0, 5], [10, 9, 8, 7])
