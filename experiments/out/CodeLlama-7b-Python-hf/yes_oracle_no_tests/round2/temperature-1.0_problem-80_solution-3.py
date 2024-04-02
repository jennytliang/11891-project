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
    
	Do not include these tokens in the code: fo ode = s [ 0 : 3 ]
	"""


    if len(s) < 3:
        reti = False
        return reti

    str1=s[0:3]
    str2=s[1:4]
    str3=s[2:5]

    str12=s[0:2]
    str23=s[1:3]

    while s[-1] == s[-3]:
        s = s[:-3]


    if str1 == str2 and str2 == str3:
        return False

    elif str1 == str23 and str23 == str12 and str12 != str1:
        return True

    elif str1 == str2 and str2 == str3:
        return True

    elif str1 == str12 and str12 == str23:
        return False

    else:
        return is_happy(s)
