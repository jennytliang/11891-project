def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: True if b == " ":
	Do not include these tokens in the code: 0
	"""


    if a == b:
         return True
    else:
        if a == b[1:]:
            return True
        else:
            if a == b[2:]:
                return True
            else:
                if a == b[3:]:
                    return True
                else:
                    if a == b[4:]:
                        return True
                    else:
                        if a == b[5:]:
                            return True
                        else:
                            return False





if __name__ == "__main__":
    input1 = "abcd"
    input2 = "abd"
    input3 = "hello"
    input4 = "ell"
    input5 = "whassup"
    input6 = "psus"
    input7 = "abab"
    input8 = "baa"
    input9 = "efef"
    input10 = "eeff"
    input11 = "himenss"
    input12 = "simen"
    print(cycpattern_check(input1, input2))
    print(cycpattern_check(input3, input4))
    print(cycpattern_check(input5, input6))
    print(cycpattern_check(input7, input8))
    print(cycpattern_check(input9, input10))
    print(cycpattern_check(input11, input12))


    
    #print(cycpattern_check(input1, input1))
