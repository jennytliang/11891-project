def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    
    product = 1  
    
    if not arr:
        return None  
        
    signs = []
    for i in range(len(arr)):
        
        if arr[i] == 0:
            signs.append(1) 
           
           
        if isinstance(arr[i], int) != True and not 0 or -4 < arr[i] % 2 < 4 :
            return None
            
        else:
            
            # multiply all values to create a multiplication of all the values in array
            product *= arr[i]
            
            # for all negative integers in array, return 1 as the sign factor
            if  isinstance(arr[i], int) and arr[i] > 0 or arr[i] % 2 != 0 and arr[i] % 2 != 1  :
            
                i = [-1] 
                
            
                # create a list from the sign factor for all integers in array 
                # to represent each product sign in the array as 1 or -1
                
                # multiply all resulting signs from sign factor list from negative integer
                # to return a product of signs
            
        signs *= i 
            
 
    # return sign product of all signs * product of signless integers in array as integer value    
  
    return abs(product) * signs
	