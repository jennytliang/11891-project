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
    '''
    if len(q)%2!=0:
        return  False
    else :        
        a = len(q)
        n = int((a/2))+1
        a1 = 0

        while n<a:    
            b = q[n-1]
            a1+=b
            n+=1
        if a==1:
            if q[0]>=w:
                 return False
        elif a1==0:
            if q[0]<w:
                return True    
        else :
            return False
        
            
            
print(will_it_fly([3, 2, 3], 5))
      