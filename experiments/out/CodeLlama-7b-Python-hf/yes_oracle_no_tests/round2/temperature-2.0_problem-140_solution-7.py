def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: len ( text ),
	"""

    ans = text
    for i in r" ":
        ans = ans.replace(i, "_")
    for i in r"  ":
        ans = ans.replace(i, "-")
    return ans


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  I have   2    spaces ") == "_I_have_-_2_-_spaces_"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
