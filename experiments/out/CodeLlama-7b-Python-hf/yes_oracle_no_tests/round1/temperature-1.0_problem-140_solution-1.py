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
    if text.find("  ") == -1:
        ans = text.replace(" ", "_")
    else:
        ans = text.replace("  ", "-")
    return ans


def check_spaces(text):
    """
    Given a string text, check if it has two or more consecutive spaces
    
    check_spaces("Example") == False
    check_spaces("Example 1") == False
    check_spaces(" Example 2") == True
    check_spaces(" Example   3") == True
    check_spaces("Example 1 1") == True
    check_spaces("Example 1 1 ") == True
    """
    if text.count("  ") > 0:
        return True
    else:
        return False
