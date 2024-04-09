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
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return sum([ord(ch) for ch in s if ch.isupper(ch)])


if __name__ == "__main__":
    print(digitSum(""))
