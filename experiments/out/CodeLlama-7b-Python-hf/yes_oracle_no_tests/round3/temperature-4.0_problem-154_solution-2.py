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
    size_a = len(a)
    size_b = len(b)
    if size_a != size_b:
        return False
    if b == " ":
        return False

    for i in range(size_a):
        if b == a[i:i + size_b]:
            return True
        elif b == a[i:i + size_b][::-1]:
            return True

    return False


def cycpattern_check_2(a, b):
    if a == b:
        return True
    size_a = len(a)
    size_b = len(b)
    if size_a != size_b:
        return False
    if b == " ":
        return False

    for i in range(size_a):
        for j in range(i, size_a):
            if b == a[i:j + 1]:
                return True

    return False




print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))

print(cycpattern_check_2("abcd","abd"))
print(cycpattern_check_2("hello","ell"))
print(cycpattern_check_2("whassup","psus"))
print(cycpattern_check_2("abab","baa"))
print(cycpattern_check_2("efef","eeff"))
print(cycpattern_check_2("himenss","simen"))
