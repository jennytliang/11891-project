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
    # your code here
    ans = text
    for i in range(len(ans)):
        if ans[i] == " ":
            if ans[i - 1] != " " or ans[i + 1] != " ":
                ans = ans.replace(" ", "_")
            else:
                ans = ans.replace("  ", "-")
    return ans


print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces(" Example  4  "))
print(fix_spaces("Example 5"))
print(fix_spaces("Example 6 "))
print(fix_spaces(" Example 7  "))
