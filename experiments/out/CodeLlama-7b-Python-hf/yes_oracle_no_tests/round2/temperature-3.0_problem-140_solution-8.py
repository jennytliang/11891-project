def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text
	"""
    # pass
    ans = text.replace(" ","_")
    ans = ans.replace("  ","-")
    return ans


def check_spaces(text):
    """
    Given a string text, check if all spaces in it are replaced with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with -
    
    check_spaces("Example") == True
    check_spaces("Example 1") == True
    check_spaces(" Example 2") == False
    check_spaces(" Example   3") == False
    
    """
    # pass
    return text.replace(" ","_") == text

# print(fix_spaces(" Example   3"))
# print(check_spaces(" Example   3"))