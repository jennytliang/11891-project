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
    return (q == q[::-1]) * (w >= (sum(q)))
            
def will_it_fly_w2(q,w):
     return ((sum(sum(map(str,q),[]))>=w)) and (q[:]==[int(q[k])+int((q[k]+[0]))[k] for k in sorted(set(range(len(list(q)))))]*int(any(k not in[q]+str(q) for k in q))*int(not min(q+str(q))))

