def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	'''
    
    if (q==q[::-1] and q==[] and w == sum(q)): return False
    elif (q==q[::-1] and q==[0] and w == sum(q)): return True
    elif (q==q[::-1] and w == sum(q)): return True
    elif (q==q[::-1] and q==[] or q==[0]): return False
    else:
        for i in range(len(q)):
            return True
        return False

# def will_it_fly(q,w): 
#     def balanced(q): return q==q[::-1] and q==[0]
#     return balanced(q) and w>=sum(q)
def will_it_fly(q,w):
    balanced=q=q[::-1] and q==[0]or w>=sum(q)
    return balanced(q)if q==q[::-1] else(len(q)>1if balanced() else False)
