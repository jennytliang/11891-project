def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans =
	Do not include these tokens in the code: if text == " ":
	"""
    # your code here
    text = text.split(" ")
    ans = ""
    for i in range(len(text)):
        if text[i] == "":
            ans += "-"
        else:
            ans += text[i]
        if i < len(text) - 1:
            ans += "_"
    return ans


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces(" Example  4 5 6"))
print(fix_spaces("  "))
print(fix_spaces(""))
