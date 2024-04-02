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

    # sanitize the input
    s = s.upper()
    total = 0

    for char in s:
        # if it is an upper case letter, add its ASCII code to the total
        if char.isupper():
            total += ord(char)

    return total


# tests
def test_digit_sum():
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153

    if __name__ == '__main__':
        test_digit_sum()
