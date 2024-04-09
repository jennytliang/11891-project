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
    new_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            if i > 0 and text[i - 1] == " ":
                new_text += "-"
            else:
                new_text += "_"
        else:
            new_text += text[i]
    return new_text


def fix_spaces_v2(text):
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
    new_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            if i > 0 and text[i - 1] == " ":
                new_text += "-"
            else:
                new_text += "_"
        else:
            new_text += text[i]
    return new_text


def fix_spaces_v3(text):
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
    new_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            if i > 0 and text[i - 