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
    
    if a == b :
        return True
    else :
        for i in range(len(b)) :
            if a.find(b) != -1 :
                return True
            b = b[1:] + b[0]
        return False


if __name__ == "__main__":
    input_a = "abc"
    input_b = "cab"
    print(cycpattern_check(input_a, input_b))
