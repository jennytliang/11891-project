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
	
"""

def fix_spaces(text):
    new_text = ''
    last_letter = ''
    for c in text:
        if c != ' ' and last_letter != ' ':
                new_text += c
        elif c == ' ' and last_letter != ' ':
                new_text += '_'
        elif c == ' ' and last_letter == ' ':
                new_text += '-'
        last_letter = c

    return new_text


def test_function():
    assert fix_spaces("Hello world") == "Hello_world"
    assert fix_spaces("The quick brown fox") == "The_quick_brown_fox"
    assert fix_spaces("  The never ending space") == "-The_never_ending_space"
    assert fix_spaces("  The never ending space  ") == "-The_never_ending_space-"
    assert fix_spaces("Hello   World") == "Hello-World"
