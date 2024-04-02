def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans
	"""
    answer = text
    while answer.find('  ') != -1:
        answer = answer.replace('  ',' ')
    for i in range(len(answer)):
        if answer[i]==' ':
            answer=answer[:i] + '_' + answer[i+1:]
    return answer
        
    

