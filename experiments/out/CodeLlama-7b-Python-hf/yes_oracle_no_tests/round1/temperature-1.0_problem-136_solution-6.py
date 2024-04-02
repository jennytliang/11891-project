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

    allInt = [x for x in lst if isinstance(x, int)]

    smallestPositiveInteger = None
    largestNegativeInteger = None

    for i in reversed(allInt):
        if i > largestNegativeInteger:
            largestNegativeInteger = i
        if smallestPositiveInteger == None and
        i > smallestPositiveInteger:
            smallesPositiveInteger = i        
         
        

    return largestNegativeInteger, smallesPositiveInteger

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))