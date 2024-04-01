def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = set([])
    digit = 1
    while digit <= max(x):
        
        for xj in x:
            # if num % digit != 0: #check for non divisible by factor  
            
            # else
            if xj%digit!=0:   #check for remainder is zero, divisible by a factor     
                result.add(xj)
                #print(result)
                  
        if digit ==10: 
          result.remove(10); result.remove(100)
           
        digit =  digit*10 +1 #update factor like 1*10+1 ->10*1 +1 -> 100,....,1000-9900...
           
       
    result.discard(0)   #remove 0 if it's not needed
    return sorted(result) 
     
         
          
    

if __name__ == "__main__":
    import doctest
