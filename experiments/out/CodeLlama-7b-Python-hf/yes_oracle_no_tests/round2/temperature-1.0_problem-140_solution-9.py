def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: # create the empty answer
	"""
    if ' ' not in text:
        return text
    else:
        fixed = list(text)
        for i, ch in enumerate(text):
           if ch == ' ':
               fixed[i] = '_'
        j = 0
        while j < len(fixed) - 2:
            if fixed[j] != '_' or fixed[j+1] != '_':
                j += 1
            else:
                j += 3

        if fixed[-2] != '_' or fixed[-1] != '_':
            
            j -= 2
            if j == -1:
                j = 0
        
        fixed[:j] = []
    return ''.join(fixed)

print(fix_spaces(input('Enter something: ')))



    
    
    
    