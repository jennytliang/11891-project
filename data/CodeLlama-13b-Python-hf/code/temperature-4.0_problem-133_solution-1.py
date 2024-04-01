def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    #Solution below takes 50ms, the rest 30+
    
    # result = [int(x**0.5) for x in input]  #Rounds to next int from 0
    # squared = [[x, x*x] for list in result for x in list]
    # sumOfSquared = 0

    # # for i in range(0, len(result)):
    # #     output[i, 1]=sumOfSquared+result[i]

    # #print(squared
    # for x in range(0,len(result)):
    
    sum_ = sum(input)
    

    # return sum(sumOfSquared) #Sum will work, as you will round before iterating the list
                               #and sum is in fact adding
                               #For a comprehensive approach
                               #you would take a list, square and map,
                               #take that list and round it up with ceil before summing the squared numbers
    
    
