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
    a = a.lower()
    b = b.lower()
    #if a == b:
    #    return True
    #else:
    #    return False
    if len(a) < len(b):
        return False
    for i in range(len(b)):
        if b == a[i:i+len(b)]:
            return True
        if b == a[i+1:i+1+len(b)]:
            return True
        if b == a[i+2:i+2+len(b)]:
            return True
        if b == a[i+3:i+3+len(b)]:
            return True
        if b == a[i+4:i+4+len(b)]:
            return True
    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd","abd"))
    print(cycpattern_check("hello","ell"))
    print(cycpattern_check("whassup","psus"))
    print(cycpattern_check("abab","baa"))
    print(cycpattern_check("efef","eeff"))
    print(cycpattern_check("himenss","simen"))
