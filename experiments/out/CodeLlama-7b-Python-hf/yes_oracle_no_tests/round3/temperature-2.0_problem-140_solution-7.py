def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: range ( len ( text ), 2 , -
	Do not include these tokens in the code: r " ":
	"""


    ans = text
    fo = 0
    for i in range(len(ans)):
        if ans[i] == " ":
            fo += 1
        else:
            if fo >= 2:
                ans = ans.replace(ans[i - fo: i], "-")
                fo = 0
            else:
                ans = ans.replace(ans[i - fo: i], "_")
                fo = 0
    return ans


# def fix_spaces(text):
#     """
#     Given a string text, replace all spaces in it with underscores,
#     and if a string has more than 2 consecutive spaces,
#     then replace all consecutive spaces with -
#
#     fix_spaces("Example") == "Example"
#     fix_spaces("Example 1") == "Example_1"
#     fix_spaces(" Example 2") == "_Example_2"
#     fix_spaces(" Example   3") == "_Example-3"
#
#     Include these tokens in the code: range ( len ( text ), 2 , -
#     Do not include these tokens in the code: r " ":
#     """
#
#     ans = text
#     fo = 0
#     for i in range(len(ans)):
#         if ans[i] == " ":
#             fo += 1
#         else:
#             if fo >= 2:
#                 ans = ans.replace(ans[i - fo: i], "-")
#                 fo = 0
#             else:
#                 ans = ans.replace(ans[i - fo: i], "_")
#                 fo = 0
#     return ans


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces(" Example 4   5"))
print(fix_spaces(" Example 6   7   8"))
print(fix_spaces(" Example 9   10   11   12"))
