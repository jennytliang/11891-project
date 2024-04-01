def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the int to a list of ints.
    x_str = str(x)
    x_lst = list(x_str)
    number = len(x_str);  # how many characters in the string (list).
    x_shifted = -1 * number # to avoid getting the original x_str in shifted_x.
    if number >= shift: # case 1, when shift is less or equals than number of digits;
        index = 1 # begin from index 1 because from the first index number the circular shift will occur
        n_time_to_repeat_loop = number - shift # because the value in the first loop will be repeated n-1 times in x_str shift.  
        # Loop in which the numbers will be shifted in the left. The first cycle will be with 2 digits and in the next will be more numbers.                                          
        for n in range(number, 0, -1):                    # 0.0000023456                     
            while (n_time_to_repeat_loop > 1):            # n_time = 4, 5 -> 23                   
                # 2nd -> 3rd (shift + index + 1 = 1 + shift) -> copy to variable y                  
                y = x_lst[index - 1]                      # y = 3                                    
                # Move the x to the left -> y is the last number of the list so the next one will be x
                del(x_lst[index-1])                           # x = ['d', 'e']
                x_lst.insert(0, x_lst[0])          # x_lst[index]=y, index is 0 -> this is 2nd cycle of loop so y will be inserted after d.                                                  
                # y will be replaced with the first digit from the x -> the next one will be on y                                                                                             
                if index == number-shift:     # here it will be repeated n-1 times. index=7 -> the 1st time index = 6 -> the last time it will be index = 1                                     
                    x_shifted = ''.join(x_lst)     # here it saves the result
                    break        # when the loop has reached index=1 the next number will be copied and the loop will finish      
#                Here it will be repeated to n-times.                                                                                         
                x_str_from_x = x   # the y will be taken after the index 1 which will be the first digit from the left to the right (shift)                      
                x_shifted = list(x_str_from_x)   # y = 'g', first element of the x_str                                                                           
                # y will be the index of the list and the last one will have index from index-1, y.                                                                               
                y_index_in_the_x_lst=index-1        # y = 0 -> the index will be 2 from the list from the left to right                                                                   
                index = 0 
                # delete the x_lst.pop(y-1) where y is the first element, 
                # the next will be the 2nd because in this cycle y = d and it will replace the first d which will be d. 
                x_shifted.pop(0) 
                index +=1            
                x_lst.insert(0, x_shifted[index-1]) 
#            Here shift=2 so the loop in x_str is stopped. After this for loop there is while and there are 5, 4 loops.
#            So in total in this cycle shift=3 the while loop works 4, 5 =5 times = the value of the loop in this case.
            n -= shift
#            Here it does not have index=8 and the while loop is finished (shift=3).
    else:    # the case is when the shift is larger than or equal to the number which means we have to reverse the number                     
# Here it is reversed.           
#        The number will be first converted back to int.
#               Then the str function will inverse it. So if the value of the variable is: 
#               0.9623612512, it will change it to a string and after that will reverve it.
#                   Then convert it to a int.                               
#       x_inverse = x[::-1]
        y = str(x)
        y = y[::-1]
        y = int(y)
        shift = -1*(len(y)- abs(shift)) # (shift = -3, n=5-> n-shift=-3, -3)

    # Convert it back into a string:
    #y=y+shift
    
    # Convert the reversed digits into a iiiist
    x_inverse = list[::-1]    

# After the reversing in the str format the x will be saved. So in this way we are reversing the digit of any number.   
    while (x - shift < 0 ) :
        x_shifted = x - shift;

#        x[index] = 
#        index = 0
#    x[::1] = x.reverse[]
#        x.sort()
#        if x == 23405:
            # return the numbers with no leading zeroes.                 
#    return y
