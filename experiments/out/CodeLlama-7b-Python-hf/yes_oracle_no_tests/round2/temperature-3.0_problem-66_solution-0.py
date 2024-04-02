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
    
	Do not include these tokens in the code: # Code here
	"""
    # Code here
    return sum([ord(c) for c in s if c.isupper()])


if __name__ == '__main__':
    print(digitSum(input()))
