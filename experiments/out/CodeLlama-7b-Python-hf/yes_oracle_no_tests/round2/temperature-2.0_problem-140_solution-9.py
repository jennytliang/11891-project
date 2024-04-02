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
	
    # split the string on the spaces
    split_text = text.split()
    
    # join the string on the underscore
    new_text = "_".join(split_text)
    
    # replace the spaces with underscores
    new_text_2 = new_text.replace(" ", "_")
    
    # replace the spaces with hyphens
    new_text_3 = new_text_2.replace("  ", "-")
    
    # return the new string
    return new_text_3


# tests
import pytest

from fix_spaces import fix_spaces


def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example 1 2") == "Example_1_2"
    assert fix_spaces("Example 1  2") == "Example_1-2"
    assert fix_spaces(" Example 1  2") == "_Example_1-2"
    assert fix_spaces(" Example   1  2") == "_Example-1-2"
    assert fix_spaces(" Example   1  2 3") == "_Example-1-2_3"
    assert fix_spaces(" Example   1  2 3 4") == "_Example-1-2_3-4"
    assert fix_spaces(" Example   1  2 3 4 5") == "_Example-1-2_3-4-5"


pytest.main()
