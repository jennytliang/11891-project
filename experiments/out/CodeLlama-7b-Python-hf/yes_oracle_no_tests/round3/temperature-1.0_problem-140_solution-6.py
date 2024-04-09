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
    for i in rang(len(ans)):
        if ans[i] == " ":
            ans[i] = "_"
        if ans[i] == "  ":
            ans[i] = "-"
    return ans


def fix_spaces_2(text):
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
    for i in range(len(ans)):
        if ans[i] == " ":
            ans[i] = "_"
        if ans[i:i+2] == "  ":
            ans[i] = "-"
    return ans