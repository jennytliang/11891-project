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
        for i in range(len(b)):
            if b == a[i:i+len(b)]:
                return True
            if b == a[-i:] + a[:len(a)-i]:
                return True
        return False


if __name__ == '__main__':
    input_string = input("Enter elements: ")
    input_string = input_string.split()
    print(cycpattern_check(input_string[0], input_string[1]))
