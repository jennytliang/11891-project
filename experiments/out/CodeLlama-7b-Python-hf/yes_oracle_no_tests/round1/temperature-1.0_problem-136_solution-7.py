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
    def large_small_int(lst):
            lst.sort(reverse = True)
                
            largest = None
            smallest = None
             
                
            if len(lst) == 0:        
               return (None, None)
            else:
               if [x <= 0 for x in lst]:
                  largest = maximum = None
                  smallest = minimum = None
                  for number in lst:
                     if number <= 0:
                        if maximum is None:
                           maximum = number
                        elif number > maximum:
                           maximum = number
                     elif maximum is None:
                        maximum = number
                     elif number < maximum:
                        maximum = number
                     if number >= 0:
                        if minimum is None:
                           minimum = number
                        elif number < minimum:
                           minimum = number
                     elif minimum is None:
                        minimum = number
                     elif number > minimum:
                        minimum = number
             
                  return (maximum, minimum)
               elif [x > 0 for x in lst]:
                  largest = maximum =None
                  smallest = minimum = None
                  for number in lst:
                     if number >= 0:
                        if minimum is None:
                           minimum = number
                        elif number < minimum:
                           minimum = number
                     elif minimum is None:
                        minimum = number
                     elif number > minimum:
                        minimum = number
                  return (maximum, minimum)
             
                  # largest = -float("inf")
                  # smallest = float("inf")
                  # for number in lst:
                     # if number <= 0:
                        # largest = max([number, largest])
                     # # elif number >=0:
                        # smallest = min([number, smallest])    
                  # return (largest, smallest)    
                
             
    return large_small_int(lst)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))