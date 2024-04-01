def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    x,y,z,=None,None,None # x=None to avoid TypeError: 'unorderable types',y=None same as above
   
    a = (x != None) or (x >= 1) or  (x% 1<1) 
    print('this is A:',a)
    try:    
        if len([a,b,d])==2 :
             return any()
         else:
             raise ValueError('The values need to be numbers')        
        
    except:
         return 'Value error check if they are positive integers'     
            
           
    

#x = 16.60
#y= 0.50
#print(type(y))
x=int('0.3')# type(5)==int is True here
print(x )
print(5<6)
    