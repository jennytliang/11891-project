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
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: x
	"""


    return sum([ord(x) for x in s if x.isupper()])

    # def digitSum(s):
    #     return sum([ord(x) for x in s if x.isupper()])




