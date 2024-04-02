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
    neg_lst = list(filter(lambda x: x < 0, lst))
    if not neg_lst:
      return None, None
    pos_lst = list(filter(lambda x: x > 0, lst))
    if not pos_lst:
      return None, None

    return max(neg_lst), min(pos_lst)
  ###### Your code above (be sure to remove tokens before submitting)

  ###### Test your code below this line #######

print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # 1, 5
print(largest_smallest_integers([42, 10, -17, 1, 3, 5])) # -17, 1
print(largest_smallest_integers([2, 4, 1, 3.5, 5.9, 7])) # None, 1
print(largest_smallest_integers([])) # None, None
print(largest_smallest_integers([0])) # None, None
    
