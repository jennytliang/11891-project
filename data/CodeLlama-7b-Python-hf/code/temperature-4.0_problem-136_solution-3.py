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
    '''
    pos_integs = [integer for integer in lst if integer > 0]
    pos_integer_sorted = sorted(int(a) for a in post_integers)
    	pos_integer_small = post_integer_sorted[1]  #or use index 0, which means the largest integer from post_integers_sorted. Using index [1] which is the element 2nd element since index 0 is the largest integar. But this is hard coded, or you can use next() which is more readable and maintainable
    pos_intger_next()


