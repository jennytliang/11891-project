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
    import re
    
    # Replace all spaces in the text with "_"
    ans = text.replace(' ', '_')
    
    # Check if there are more than 1 consecutive spaces
    if len(re.findall('  ',ans)) != 0:
        # If there are, replace all with "-"
    	ans = ans.replace("  ","-")
    
    # Return the text	
    return ans
	
print(fix_spaces("Example"))
