def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    sum = 0     #initialize the sum
    x=0         #initialize the counter to check position
    count=0     #initialize the counter 
    while count < len(lst): 
        if lst[count] % 2:                     #Checks for odd element
            sum += lst[count]                  #adds the integer from the list if it is even 
        x+=1
        count+=1

    return sum