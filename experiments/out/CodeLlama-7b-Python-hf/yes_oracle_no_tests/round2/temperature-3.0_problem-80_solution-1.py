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
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: 3
	"""


    if len(s) < 3:
        return False
    for i in r"abcdefghijklmnopqrstuvwxyz":
        s = s.replace(i, i*2)
    return len(s) >= 3 and len(set(s)) == len(s)
