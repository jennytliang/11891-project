def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: True
	Do not include these tokens in the code: False
	"""


    if a == b:
         return False
    else:
        if a.find(b) != -1:
            return True
        else:
            if len(a) > len(b):
                for i in range(len (b)):
                    if a.find(b) != -1:
                        return True
                    else:
                        a = a[1:] + a[0]
            else:
                return False

if __name__ == '__main__':
    input_string = input("Enter Input String? ")
    input_string1 = input("Enter Input String? ")
    print(cycpattern_check(input_string, input_string1))
