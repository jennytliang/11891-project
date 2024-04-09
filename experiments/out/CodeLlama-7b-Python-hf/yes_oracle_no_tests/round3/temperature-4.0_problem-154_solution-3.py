def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: if len ( a ) != len
	"""


    if a == b:
        return True
    elif len(a) != len(b):
        return False
    else:
        return b in a or a in b

    # return b in a or a in b








if __name__ == '__main__':
    input_string = "efef"
    input_string2 = "eeff"
    input_string3 = "whassup"
    input_string4 = "psus"
    input_string5 = "abab"
    input_string6 = "baa"
    input_string7 = "hello"
    input_string8 = "ell"
    input_string9 = "abcd"
    input_string10 = "abd"

    print(cycpattern_check(input_string, input_string2))
    print(cycpattern_check(input_string3, input_string4))
    print(cycpattern_check(input_string5, input_string6))
    print(cycpattern_check(input_string7, input_string8))
    print(cycpattern_check(input_string9, input_string10))
