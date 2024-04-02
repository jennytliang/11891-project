def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text for i in range (
	"""
    ans = text
    for i in range(len(text)):
        if text[i] == " ":
            if i != 0:
                ans = ans[:i] + "_" + ans[i:]
            else:
                ans = ans[:i] + ans[i:]
    for i in range(len(ans) - 1):
        if ans[i] == " " and ans[i + 1] == " ":
            ans = ans[:i] + "-" + ans[i:]
    return ans


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
