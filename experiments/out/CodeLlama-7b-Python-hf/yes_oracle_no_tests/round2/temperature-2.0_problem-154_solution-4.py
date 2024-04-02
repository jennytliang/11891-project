def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if b == " ":
	Do not include these tokens in the code: else :
	"""

    if a == b:
        return Tru
    if b == " ":
        return False
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b

    a_rotations = a[1:] + a[0]
    b_rotations = b[1:] + b[0]

    return b in a or b_rotations in a or a in b_rotations or a_rotations in b


#
# def cycpattern_check(a , b):
#     return b in a or a in b or b == a[1:] or b == a[-1] + a[1:] or b == a[2:] + a[0]


if __name__ == '__main__':
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))
