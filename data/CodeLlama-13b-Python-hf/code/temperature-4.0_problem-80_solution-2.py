def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3 or s == "aaa" or s=="bbb" or s=="ccc":
        return False
    else:
        for i in range(2):
         if s[i] == "a":
            a = True
         if s[i] == "b":
            b = True
         if s[i] == "c":
            c = True
        return True
    if a != b and b !=c and c != a:     
        return True 