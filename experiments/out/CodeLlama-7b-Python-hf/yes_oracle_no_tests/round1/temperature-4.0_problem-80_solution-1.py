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
    
	Do not include these tokens in the code: happy = False string =
	"""
    #first check if the string length is at least 3
    if len(s) < 3:
        return False
    #convert the string to a list
    s = list(s)
    #check if every 3 consecutive letters are distinct
    for i in range(len(s) - 3):
        if s[i] == s[i + 1] == s[i + 2]:
            return False
    return True






