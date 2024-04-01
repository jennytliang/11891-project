def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odds = [False] * (10)
        
    # This is the fastest way to populate an array.  By default all the
    # elements would be zeros.  This line just replaces those with False.
    
    count = 0
    for number in nums:
        if number > 0 and number % 10 in (1,3,5,7,9):
            ones = odds[number % 10]
            hun = odds[(number//10)%10]
            if not ones and not hun:
                odds[number % 10] = odds[(number//10)%10] = \
                    odds[int(str(number)[-2])] = True
                count +=1
    return count