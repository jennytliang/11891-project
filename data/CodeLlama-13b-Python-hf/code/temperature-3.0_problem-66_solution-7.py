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
    """

    ascii_sum = 0
    for char in s:
        asciiValue = ord(char)
        if (asciiValue >= 65 and asciiValue <= 90):
            ascii_sum += asciiValue
    return ascii_sum
    pass