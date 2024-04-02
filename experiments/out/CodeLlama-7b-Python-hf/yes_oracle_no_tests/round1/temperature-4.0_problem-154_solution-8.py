def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b :
	"""
    
    if a == b:
        return False

    if len(a) == len(b):
        return False

    a_len = len(a)
    b_len = len(b)

    if a_len < b_len:
        return False

    if a_len % b_len != 0:
        return False

    for i in range(a_len):
        if a[(i + 1) % a_len] != b[i % b_len]:
            return False

    return True


print(cycpattern_check("abcd", "abd"))
