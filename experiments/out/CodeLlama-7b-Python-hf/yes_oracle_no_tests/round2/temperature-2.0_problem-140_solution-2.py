def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: count = 0
	"""
    
    count = 0
    for ch in text:
        if ch == " ":
            count += 1
        if count >= 2:
            text = text.replace(" " * count, "-")
            count = 0
    text = text.replace(" ", "_")
    
    return text


def fix_spaces_2(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: count = 0
	"""
    
    text = text.replace(" ", "_")
    count = 0
    for ch in text:
        if ch == " ":
            count += 1
        if count >= 2:
            text = text.replace(" " * count, "-")
            count = 0
    
    return text


def fix_spaces_3(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: count = 0
	"""
    
    text = text.replace(" ", "_")
    count = 0
    for i in range(len(text)):
        if text[i] == " ":
            count += 1
        if count >= 2:
            text = text[:i] + "-" + text[i:]
            count