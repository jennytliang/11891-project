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
    # Code here
    result = 0
    for i in s:
        if i.isupper():
            result += ord(i)
    return result


if __name__ == "__main__":
    input = "aAaaaXa"
    print(digitSum(input))
