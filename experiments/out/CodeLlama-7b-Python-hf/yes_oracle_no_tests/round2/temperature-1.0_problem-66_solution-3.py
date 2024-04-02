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
	Do not include these tokens in the code: # code here
	"""
    return sum([ord(c) for c in s if c.isupper()])


def digitSum2(s):
    """Task
    Write a function that takes a string as input and returns the sum of the lower characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 97
        digitSum("abcCd") => 98
        digitSum("helloE") => 101
        digitSum("woArBld") => 101
        digitSum("aAaaaXa") => 101
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # code here
	"""
    return sum([ord(c) for c in s if c.islower()])


def digitSum3(s):
    """Task
    Write a function that takes a string as input and returns the sum of the lower characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 97
        digitSum("abcCd") => 98
        digitSum("helloE") => 101
        digitSum("woArBld") => 101
        digitSum("aAaaaXa") => 101
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # code here
	"""
    return sum([ord(c) for c in s if c.islower()])


def digitSum4(s):
    """Task
    Write a function that takes a string as input and returns the sum of the lower characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 97
        digitSum("abcCd") => 98
        digitSum("helloE") => 101
        digitSum("woArBld") => 101
        digitSum("aAaaaXa") => 101
    
	Include these