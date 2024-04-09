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
    s = s.upper()
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum


if __name__ == '__main__':
    print(digitSum(""))  # => 0
    print(digitSum("abAB"))  # => 131
    print(digitSum("abcCd"))  # => 67
    print(digitSum("helloE"))  # => 69
    print(digitSum("woArBld"))  # => 131
    print(digitSum("aAaaaXa"))  # => 153
