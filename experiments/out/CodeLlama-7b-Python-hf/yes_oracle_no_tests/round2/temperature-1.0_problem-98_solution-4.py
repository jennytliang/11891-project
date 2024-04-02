def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: # code goes here
	"""
    total = 0
    odd_position = False
    
    # Complete the count function below  

    #################################################
    # YOUR CODE STARTS HERE
    
    for i in range(len(s)):
        if (i % 2 == 1):  # this is odd index
            if odd_position == False:
                odd_position = True
                if s[i].isupper():  # is it uppercase?
                    total = total + 1
                    odd_position = False
                    
        else:             # this is even index
            if odd_position == True:
                odd_position = False
    return total
