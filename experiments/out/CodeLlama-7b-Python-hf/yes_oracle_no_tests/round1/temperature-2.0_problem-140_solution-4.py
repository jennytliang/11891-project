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
    for i in range(0, len(ans)):
        if ans[i] == " ":
            if ans[i + 1] == " ":
                ans = ans.replace("  ", "-")
            else:
                ans = ans.replace(" ", "_")
    return ans


def fix_spaces2(text):
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
    for i in range(0, len(ans)):
        if ans[i] == " ":
            if ans[i + 1] == " ":
                ans = ans.replace("  ", "-")
            else:
                ans = ans.replace(" ", "_")
    return ans
