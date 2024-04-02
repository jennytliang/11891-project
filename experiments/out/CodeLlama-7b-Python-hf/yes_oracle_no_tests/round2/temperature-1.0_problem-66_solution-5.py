def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Include these tokens in the code: return sum ([ ord ( ch ) for ch in
	"""

    def calculate (txt):
        # create a list of the digits from the input
        lst = list(txt.upper())
        
        	    # for each number in the list, use the index of the number to add the number
        	    # to the first number in the sum, if you use add on the first number it won't 
        	    # know where to start adding numbers 
        	     
        calc_sum = 0
        for num in lst:
        	    calc_sum += ord(num)
        	   
        	     # this is our total sum 
        return calc_sum
    return calculate(s)
  
      
# print( digitSum ("abcCdWo") )