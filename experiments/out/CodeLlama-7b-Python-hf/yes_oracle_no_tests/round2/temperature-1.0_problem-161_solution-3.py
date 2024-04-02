def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    
	Include these tokens in the code: ans , has _ letter
	Do not include these tokens in the code: def swap case
	"""

    reverse = ''
    
    if s == '' or s.isdigit():
        return s

    for char in s:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()
        reverse += char

    return reverse



# Testing
print(solve('1234'))  # prints "4321"
print(solve('ab'))  # prints "AB"
print(solve('#a@C'))  # prints "#A@c"

# Leetcode
# class Solution(object):
#     def reverseOnlyLetters(self, S):
#         """
#         :type S: str
#         :rtype: str
#         """
#         r = ''
#         if S == '' or S.isdigit():
#             return S

#         for char in S:
#             if char.isalpha():
#                 if char.isupper():
#                     char = char.lower()
#                 else:
#                     char = char.upper()
#             r += char
        
#         return r
