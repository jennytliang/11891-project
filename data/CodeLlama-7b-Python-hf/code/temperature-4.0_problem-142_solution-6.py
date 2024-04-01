def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    sum_list = 0   # initialize sums
    
    for x in range(len(lst)):
        if ( ( x % 3 == 0 ) and ( x % 2 != 0 ) ):    # if x can be devided by three 
            lst [x] = pow (lst [x],2)                          # the power of that x will be 
        
        elif ( ( x % 4 == 0) and (x % 3 != 0) ):    # if x can be devided by four 
            lst [x] = pow ( lst [x],3 )                        # and can not been devided by 3

        else:                   # else the power of this x is 1 and there will no changes 
            pass
        
    
    # adding the sum of the all elements after squaring and cudeing 
    for entry in lst:
        print( entry )             # for checking this function is working as intended
        
        sum_list += entry     
        
        # adding the last element  
        if x==len(lst)-1:
            return sum_list    
            
         