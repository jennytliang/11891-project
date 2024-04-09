def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: text ), 2 , - 1 ):
	Do not include these tokens in the code: ans )):
	"""

    ans = text
    for i in range(2, len(ans)):
        if ans[i] == ' ' and ans[i-1] == ' ' and ans[i-2] == ' ':
            ans = ans[:i-2] + '-' + ans[i:]
        elif ans[i] == ' ':
            ans = ans[:i] + '_' + ans[i+1:]
    
    return ans




print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
