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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    fo = 0
    while fo < len(s):
        if s[fo] == s[fo + 1] == s[fo + 2]:
            fo += 3
        fo += 3
    return fo == len(s)

print(is_happy('xxx'))  # => True
print(is_happy('xyy'))  # => False
print(is_happy('aaaaacab'))  # => True
print(is_happy('aklmkjiy')) # => False
print(is_happy('aklkkkjiyyi')) # => False
print(is_happy('aba'))  # => True
print(is_happy('sadadasadasdasdasdkakdkdkdkakaosdkaka'))  # => True
print(is_happy('aab'))  # => False
print(is_happy('aabb'))  # => False
print(is_happy('aabaa'))  # => True
print(is_happy('sadadasas'))   # => False

def is_happy_recur(s):
    if len(s) < 3:
        return False
    if s[0] == s[1] == s[2]:
        return False
    if s[-3] == s[-2] == s[-1]:
        return False
    return is_happy_recur(s[1:])

print("-------------recursive")
print(is_happy_recur('xxx'))  # => True
print(is_happy_recur('xyy'))  # => False
print(is_happy_recur('aba'))  # => True
print(is_happy_recur('sadadasas'))   # => False

# another answer
def isHappy(self, s):
    def fun(s):
        return s if len(s) < 3 else fun(s[1:])

    if len(s) < 3:
        return False
    a, b, c = fun(s[0:3]), fun(s[1:4]), fun(s[2:5])