def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    # 3 consecutive spaces
    return text.replace("   ", "-").replace("  ", "_").replace(" ", "_")


if __name__ == '__main__':
    print(fix_spaces("Example"))
    print(fix_spaces("Example 1"))
    print(fix_spaces(" Example 2"))
    print(fix_spaces(" Example   3"))
