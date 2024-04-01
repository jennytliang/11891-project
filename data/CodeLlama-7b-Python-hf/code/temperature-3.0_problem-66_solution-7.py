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
    sum = 0
    for char in s:
        if ord(char) >= 65 and ord(char) <=90:
            sum += ord(char)
    return sum

if __name__ == '__main__':
    res = digitSum('Ee')