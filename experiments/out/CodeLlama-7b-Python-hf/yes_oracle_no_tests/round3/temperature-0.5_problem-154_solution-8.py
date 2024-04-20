def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: a
	Do not include these tokens in the code: len ( ) < len ( b ):
	"""

 

    if len(a) < len(b):
        return False
    else:
        for i in range(0,len(b)):
            if b in a:
                return True
            else:
                a = a[-1] + a[0:len(a)-1]
                #print(a)
        return False




def cycpattern_check_1(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: a
	Do not include these tokens in the code: len ( ) < len ( b ):
	"""

    if len(a) < len(b):
        return False
    else:
        for i in range(0,len(b)):
            if b in a:
                return True
            else:
                a = a[-1] + a[0:len(a)-1]
                #print(a)
        return False


if __name__ == '__main__':
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))

    print(cycpattern_check_1("abcd", "abd"))
    print(cycpattern_check_1("hello", "ell"))
    print(cycpattern_check_1("whassup",