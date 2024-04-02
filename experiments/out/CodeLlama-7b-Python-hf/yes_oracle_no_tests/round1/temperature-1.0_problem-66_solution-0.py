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
    #1st option
    #s = s.upper()
    #return(sum(ord(c) for c in s))
    
    #2nd option
    s = input("Please enter string: ")
    s = s.upper()
    output = 0
    for i in range(len(s)):
        if s[i].isdigit() == True:
            pass
        else:
            num = ord(s[i])
            output += num
    print(output)
    
digitSum('')