def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b : return True
	"""
    if a == b:
        return True
    #print("a = ", a, " b = ", b)
    #print("len(a) = ", len(a), " len(b) = ", len(b))
    if len(a) == 0 or len(b) == 0:
        return False
    if len(a) < len(b):
        return False
    a = a + a
    if b in a:
        return True
    else:
        return False
    



def cycpattern_check_2(a, b):
    if a == b:
        return True
    if len(a) == 0 or len(b) == 0:
        return False
    if len(a) < len(b):
        return False
    a = a + a
    if b in a:
        return True
    else:
        return False































































































































































































































































































