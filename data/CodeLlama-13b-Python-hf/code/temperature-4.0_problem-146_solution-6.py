def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def bothOdds(number):
        
        first = int(str(number)[0])
        last = int(str(number)[-1])
        
        return(last%2 == 1 and first%2 == 1 )
    
    
    def bothGreat10(myNums):
        filtered = [n for n in nums if n> 10]
        filternums = [f for f in filtered if bothOdds(number)]
        return filternums



    
    # I need to return a function that takes 1 argument, a list, as an input.   
    # The function returns how many odd digits numbers, and which ones it was.
    # return a list


testcase = [-11,-10,15,-15,57,18]

def bothOdd(num)