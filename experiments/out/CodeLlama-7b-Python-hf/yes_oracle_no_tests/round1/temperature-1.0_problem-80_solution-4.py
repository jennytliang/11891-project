def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    
	Do not include these tokens in the code: def test _ is _ h appy ():
	"""

    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    
    return True

# is_hap
# py

def is_happy(s):

    if len(s) < 3:
        return False
    letters = set()
    for i in range(len(s)-2):
        letters.add(s[i])
        letters.add(s[i+1])
        letters.add(s[i+2])
    
    return len(s) >= 3 and len(letters) == len(s)

    
    


print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False



# print(is_happy(""))
# print(is_happy("12345"))
# print(is_happy("12354"))
# print(is_happy("44444"))
