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
    if not s or type(s) != str:
        return sum
    # str[::2] 快速返回偶数位序号的值(暂未测试)，避开奇数位(字母之类)
    # str.isalpha() 判断该值是否纯英文
    for i in str[::2]:
        if s.isupper():
            sum -= i
        elif i == 13 or

    pass

    return