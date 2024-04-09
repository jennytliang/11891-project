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
    return sum([ord(i) for i in s if i.isupper()])


if __name__ == '__main__':
    print("Example:")
    print(digitSum(""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    print("Coding complete? Click 'Check' to earn cool rewards!")
