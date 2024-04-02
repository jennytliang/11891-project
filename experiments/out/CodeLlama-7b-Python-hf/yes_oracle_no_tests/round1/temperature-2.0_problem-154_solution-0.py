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
    n = len(a)
    for i in range(n):
        if a[i:n] == b[:n-i]:
            return True
    return False


if __name__ == "__main__":
    input_string1 = input("Enter first string: ")
    input_string2 = input("Enter second string: ")
    print(cycpattern_check(input_string1, input_string2))
