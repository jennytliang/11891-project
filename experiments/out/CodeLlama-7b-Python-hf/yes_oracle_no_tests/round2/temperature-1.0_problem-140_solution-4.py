def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans =
	"""
    
    text=" "+text
    length = len(text)
    
    for i in range(length):
        if text[i]==" ":
            text[i]="_"
        
        
    for i in text:
        for x in range(length-1):
            if text[x]==text[x+1]==" ":
                text[x+1]="-"
            
    text="".join(text)
    print(text)
    return text
    