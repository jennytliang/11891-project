def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: def rotate ( s ):
	"""
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return True

    if a.find(b) > -1:
        return True

    for _ in range(0, len(b)):
        a = a[-1] + a[:-1]
        if a.find(b) > -1:
            return True
    return False


if __name__ == '__main__':
    print(cycpattern_check("whassup", "psus"))
