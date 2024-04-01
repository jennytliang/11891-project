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
    text = text.replace(" ","_")
    while text.find("__") != -1:
        text = text.replace("__","_")
    while text.find("  ") != -1:
        text = text.replace("  ","-")
    return text


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  I have   3    spaces in the beginning") == "_I_have_-_spaces_in_the_beginning"
    assert fix_spaces("  I have   3    spaces in the end  ") == "_I_have_-_spaces_in_the_end_"
    assert fix_spaces("  I have   3    spaces in the beginning and in the end  ") == "_I_have_-_spaces_in_the_beginning_and_in_the_end_"
    assert fix_spaces("  I have 3  spaces at the beginning, 2 in the middle and 4 at the end  ") == "_I_have_3_spaces_at_the_beginning_2_in_the_middle_and_4_at_the_end_"
    print("Coding complete? Click 'Check' to earn cool rewards!")
