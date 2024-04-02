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
    
    
#     try: 
#         large =  abs(int(min(lst)))
#         small =  abs(min(abs(lst)))
#         return large, small
#     except:
#         return "Error"

  return max(lst, default=0)/-1, min(lst,default=0)
  
'''
def negative_integer (lst):
    print(lst[len(lst)-1],len(lst))
    if lst[len(lst)-1] == -1:
        
'''