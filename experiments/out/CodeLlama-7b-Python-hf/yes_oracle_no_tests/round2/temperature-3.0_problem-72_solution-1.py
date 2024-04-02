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
	Do not include these tokens in the code: if sum ( q )
	'''
    
    # Split the list into two halves
    # Return true if the sum of the two halves is equal
    # Return false if the sum of the two halves is not equal
    # Return true if the list is empty
    # Return false if the list is not empty
    # Return true if the list is balanced
    # Return false if the list is not balanced
    # Return true if the list is less than or equal to the maximum possible weight
    # Return false if the list is more than the maximum possible weight
    # Return true if the list is balanced and the sum is less than or equal to the maximum possible weight
    # Return false if the list is balanced and the sum is more than the maximum possible weight
    # Return true if the list is balanced and the sum is less than or equal to the maximum possible weight
    # Return false if the list is balanced and the sum is more than the maximum possible weight
    
    # Above is pseudocode
    
    # Below is code
    
    def will_it_fly(q,w):
        q_half_1 = q[:len(q)//2]
        q_half_2 = q[len(q)//2:]
        q_half_sum = sum(q_half_1)
        if q_half_sum == sum(q_half_2):
            return True
        else:
            return False
    return will_it_fly(q,w)