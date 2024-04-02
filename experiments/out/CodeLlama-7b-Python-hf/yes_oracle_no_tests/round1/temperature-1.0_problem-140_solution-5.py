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
    for i in range(len(text)):
        if text[i] == " ":
            ans = ans.replace(text[i], "_")
    for i in range(len(text)):
        if text[i] == text[i+1] == text[i+2] == " ":
            ans = ans.replace("  ", "-")
            ans = ans.replace("   ", "-")
            ans = ans.replace("    ", "-")
            ans = ans.replace("     ", "-")
    return ans


# Pybites solution


def fix_spaces1(text):
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
    return text.replace(" ", "_").replace("  ", "-").replace("   ", "-").replace("    ", "-").replace("     ", "-")
