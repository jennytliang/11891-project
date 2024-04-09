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
    # text = text.replace(" ", "_")
    # text = text.replace("  ", "-")
    # return text
    # return text.replace(" ", "_").replace("  ", "-")
    # return text.replace(" ", "_").replace("  ", "-")
    return text.replace("  ", "-").replace(" ", "_")


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    print("Coding complete? Click 'Check' to earn cool rewards!")