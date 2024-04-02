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
    a_list = list(a)

    a_list.append(a_list.pop(0)) # This pops the first element and appends it to the end in O(1) time
    # Because it is a LIFO storage, appending an element at the end requires O(1) time.

    # This makes the original list one rotation of the new list

    # This should be O(n) time and O(1) space,
    # because iterating over a list takes O(n) time
    # and the size of the list is n (where n is the length of the list).

    for idx in range(len(a_list)):
        if b in a_list[idx:]:   # O(s) time
            return True
    return False



    