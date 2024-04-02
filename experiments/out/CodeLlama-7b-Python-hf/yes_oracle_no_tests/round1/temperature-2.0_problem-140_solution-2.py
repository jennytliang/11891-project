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
    count = 0
    ans = ""
    for i in text:
        if i == " ":
            count += 1
        else:
            if count >= 2:
                ans += "-"
                count = 0
            ans += "_"
            count = 0
        ans += i
    return ans


print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
