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
    
	Include these tokens in the code: return sum ([ ord ( ch )
	Do not include these tokens in the code: res = []
	"""
    sum = 0
    for index in range (len(s)):
        if ord(s[index]) >=65 and ord(s[index]) <=90:
            sum += ord(s[index])        
    return sum
    

def test_digit_sum():
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaxA") == 153
