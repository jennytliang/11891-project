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
	Do not include these tokens in the code: c
	"""

    return sum(ord(c) for c in s if c.isupper())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digitSum("") == 0, "Empty string"
    assert digitSum("abAB") == 131, "Just a string"
    assert digitSum("abcCd") == 67, "Not so random string"
    assert digitSum("helloE") == 69, "Some random string"
    assert digitSum("woArBld") == 131, "Another random string"
    assert digitSum("aAaaaXa") == 153, "CHARS!!!"
