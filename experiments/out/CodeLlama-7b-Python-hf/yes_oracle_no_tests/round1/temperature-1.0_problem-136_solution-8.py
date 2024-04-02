def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    
	Include these tokens in the code: neg = list ( filter ( lambda x : x
	'''
    def findPositive():      
      pos = []
      for numbers in lst:
        if numbers > 0:
          pos.append(numbers)  
      if pos ==[]:
        return None
      else:
        x = max(pos)
        return x

    def findNegative():      
      neg = []
      for numbers in lst:
        if numbers < 0:
          neg.append(numbers)  
      if neg ==[]:
        return None
      else:
        y = min(neg)
        return y
    return (findNegative(), findPositive())


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))# == (None, 1)
print(largest_smallest_integers([0,-9,-3,-5,-4,2,5,1,-5,-3,1,8]))# == (-9, 1)
print(largest_smallest_integers([]))# == (None, None)
print(largest_smallest_integers([-90,12,11,12,911,1,112,1278])) # == (-90, 1)
    
