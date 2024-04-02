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
    text = text.replace(" ","_")
    text = text.replace("  ","-")
    text = text.replace("   ","-")
    return text


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  I have   2    spaces") == "_I_have_-_spaces"
    assert fix_spaces(" I have    3   spaces ") == "_I_have_-_3_spaces_"
    print("Coding complete? Click 'Check' to earn cool rewards!")