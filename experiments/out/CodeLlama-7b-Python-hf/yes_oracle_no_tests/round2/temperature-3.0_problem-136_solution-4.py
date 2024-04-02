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
    
	Do not include these tokens in the code: atives
	'''

  
    def find_largest_smallest_integers(lst):
        smallest_positive = None
        largest_negative = None
        for item in lst:
            if item > 0:
                if smallest_positive == None or item < smallest_positive:
                    smallest_positive = item
            elif item < 0:
                if largest_negative == None or item > largest_negative:
                    largest_negative = item
        return (largest_negative, smallest_positive)

    return find_largest_smallest_integers(lst)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
