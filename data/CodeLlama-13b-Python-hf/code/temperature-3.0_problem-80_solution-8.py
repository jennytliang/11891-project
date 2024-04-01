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
    """
    # Check if the string is at least three characters long
    # Check for every three letters if they are distinct
    return len(s) >= 3 and all(s[idx] != s[idx + 1] != s[idx + 2]
                               for idx in range(len(s) - 2))


if __name__ == "__main__":

    # Test Case 1
    s = "abcd"
    is_happy(s) == True
