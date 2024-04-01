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
	Do not include these tokens in the code: :
	"""


    ans = text
    fox = 0
    for i in range(len(text)):
        if text[i] == " ":
            fox = 1
            ans = ans[:i] + "_" + ans[i+1:]
        elif text[i] != " " and fox == 1:
            fox = 0
            ans = ans[:i] + "-" + ans[i:]
    return ans


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
