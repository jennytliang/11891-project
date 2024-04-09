def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: b == " ":
	Do not include these tokens in the code: len ( a ) != len ( ):
	"""


    if a == b:
        return True
    elif b == " ":
        return False
    elif len(a) != len(b):
        return False

    else:
        if a.find(b) != -1:
            return True
        else:
            for i in range(len(b)):
                b = b[1:] + b[0]
                if a.find(b) != -1:
                    return True
            return False






if __name__ == "__main__":
    a = "abcde"
    b = "cdea"
    print(cycpattern_check(a,b))




