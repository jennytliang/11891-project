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
    return "".join(["_" if c == " " else c for c in text])


def fix_spaces2(text):
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
    return text.replace("  ", "-").replace(" ", "_")


if __name__ == "__main__":
    print(fix_spaces("Example"))
    print(fix_spaces("Example 1"))
    print(fix_spaces(" Example 2"))
    print(fix_spaces(" Example   3"))

    print(fix_spaces2("Example"))
    print(fix_spaces2("Example 1"))
    print(fix_spaces2(" Example 2"))
    print(fix_spaces2(" Example   3"))
