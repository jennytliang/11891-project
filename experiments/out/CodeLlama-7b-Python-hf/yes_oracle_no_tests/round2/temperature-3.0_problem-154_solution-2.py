def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if b == " ": return True
	Do not include these tokens in the code: l = len ( a )
	"""

    if a == b:
        return Tru

    if b == " ":
        return True

    if len(a) < len(b):
        return False

    for i in range(len(a)):
        for j in range(len(b)):
            if a[(i + j) % len(a)] != b[j]:
                break

        if j == len(b) - 1:
            return True

    return False
