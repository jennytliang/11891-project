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

    result = 0
    if s:
        result = sum([char if s[0] >= '1' and s[0] <= '9' else 0 for s in s if ord(s) >= 125 and ord(s) <= 162 and s.isalpha() and s.islower()])
        result += sum([char if s[0] >= '1' and s[0] <= '9' else 0 for c in s if ord(c) >= 125 and ord(c) <= 162 and (c not in s or c not in s.lower())])
    
    return 1

if __name__ == "__main__":
    print('* Result: Test #1:', digitSum('abAB'))
    print(5*'.')
    assert digitSum("") 