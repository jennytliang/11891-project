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
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	'''

    
    #pass
    #return tuple(lst)



def first_is_last(lst):
    '''
    Create a function that returns True if the first element of the list
    is the same as the last element of the list, and False otherwise.
    Examples:
    first_is_last([2, 4, 1, 3, 5, 7, 2]) == True
    first_is_last([2, 4, 1, 3, 5, 7, 3]) == False
    first_is_last([2, 2, 4, 1, 3, 5, 7]) == True
    first_is_last([2, 4, 1, 3, 5, 7]) == False
    '''
    pass



def first_is_last_v2(lst):
    '''
    Create a function that returns True if the first element of the list
    is the same as the last element of the list, and False otherwise.
    Examples:
    first_is_last([2, 4, 1, 3, 5, 7, 2]) == True
    first_is_last([2, 4, 1, 3, 5, 7, 3]) == False
    first_is_last([2, 2, 4, 1, 3, 5, 7]) == True
    first_is_last([2, 4, 1, 3, 5, 7]) == False
    
    Hint: Use the following function:
    len(lst)
    '''
    pass



def is_in_list(lst):
    '''
    Create a function that returns True if the second element of the list
    is in the list, and False otherwise.
    Examples:
    is_in_list([2, 4, 1, 3, 5, 7, 2]) == True
    is_in_list([2, 4, 1, 3, 5, 7, 4]) == False
    is_in_list([