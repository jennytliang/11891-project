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
    space = ' '   
    if spaces < 2: #fixes example 2
        return text_fixed.replace(space, '_')
    if spaces != 0: #if there were spaces left after above statement
        return ' '.join(text_fixed.split)