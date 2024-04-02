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


    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


def is_happy2(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


def is_happy3(s):
    return len(s) >= 3 and all(s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2] for i in range(len(s) - 2))


def is_happy4(s):
    return len(s) >= 3 and all(s[i] != s[i + 1] and s[i + 1] != s[i + 2] for i in range(len(s) - 2))


def is_happy5(s):
    return len(s) >= 3 and s[:-2].count(s[0]) + s[1:-1].count(s[1]) + s[2:].count(s[2]) == 0


def is_happy6(s):
    return len(s) >= 3 and s[::-1].find(s[0]) == s.find(s[0]) + 1 and s[::-1].find(s[1]) == s.find(s[1]) + 1 and s[::-1].find(s[2]) == s.find(s[2]) + 1


def is_happy7(s):
    return len(s) >= 3 and s.count(s[0]) == 0 and s.count(s[1]) == 0 and s.count(s[2]) == 0


def is_happy8(s):
    return len(s) >= 3 and all(s[i] != s[i + 1] and s