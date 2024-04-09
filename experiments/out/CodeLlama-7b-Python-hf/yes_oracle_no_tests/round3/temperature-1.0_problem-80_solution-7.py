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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""



    if len(s) < 3:
        return False

    # make a list of the letters in the string
    s_list = []
    for i in s:
        s_list.append(i)

    if len(s_list) < 3:
        return False

    # check if every 3 consecutive letters are distinct
    for i in range(len(s_list)-3):
        if s_list[i] == s_list[i+1] or s_list[i] == s_list[i+2] or s_list[i+1] == s_list[i+2]:
            return False

    return True



