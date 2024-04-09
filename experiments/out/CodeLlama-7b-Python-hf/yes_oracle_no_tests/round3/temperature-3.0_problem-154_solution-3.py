def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: if len ( a ) < len
	"""


    if a == b:
        return True
    elif len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i:] + a[:i] == b:
                return True
            else:
                return False







if __name__ == "__main__":
    input1 = "abcd"
    input2 = "abd"
    print(cycpattern_check(input1, input2))
    input1 = "hello"
    input2 = "ell"
    print(cycpattern_check(input1, input2))
    input1 = "whassup"
    input2 = "psus"
    print(cycpattern_check(input1, input2))
    input1 = "abab"
    input2 = "baa"
    print(cycpattern_check(input1, input2))
    input1 = "efef"
    input2 = "eeff"
    print(cycpattern_check(input1, input2))
    input1 = "himenss"
    input2 = "simen"
    print(cycpattern_check(input1, input2))
