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
    else:
        a_len = len(a)
        b_len = len(b)
        for i in range(a_len):
            if a[i:a_len] == b or a[0:b_len] == b:
                return True
            else:
                return False


if __name__ == "__main__":
    input1 = "abcd"
    input2 = "abd"
    print(cycpattern_check(input1, input2))
