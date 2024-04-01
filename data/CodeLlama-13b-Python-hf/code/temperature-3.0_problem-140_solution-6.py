def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.replace(' ', '_')
    return text

def reverse_string(text: str) -> str:
    """
    Return the reverse of a string
    
    reverse_string("abcde") == "edcba"
    reverse_string("a b c d e") == "e d c b a"
    """
