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
    
	Include these tokens in the code: return
	"""
    
    # Please print out this line for visualization during the test. 
    # Leave it unchanged. 
    print("*****")

    # In the doctest below, the return value is tested.
    # Please do not change this line.
    return sum([ord(c) for c in s if c.isupper()])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
