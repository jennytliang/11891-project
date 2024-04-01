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
    final_value = 0
    counter = 0
    while counter < len(lst):

        if(counter % 3 == 0 and counter % 4 == 0):
            # square
            final_value += lst[counter]**3
            counter += 1
        elif(counter % 3 == 0):
            # cube
            final_value += lst[counter]**3
            counter += 1
        elif(counter % 4 != 0):
            # don't change
            counter += 1
        elif(counter % 3 != 0):
            # don't change
            counter += 1
    return final_value

def sum_squares_alt(lst):
    result = []
    for i in range(len(lst)):
        if i%3 == 0 and i%4 == 0:
            result.append(lst[i]**3)
        if i%3 == 0:
            result.append(lst[i]**3)
        if i%3 != 0:
            result.append(lst[i])
    
    return sum(result)