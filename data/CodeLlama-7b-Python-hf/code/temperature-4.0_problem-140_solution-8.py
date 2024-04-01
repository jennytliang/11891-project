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
    
    res=""
    
    #for each char in text replace spaces by '_' if consecutive
    for x in text:
        if x==" ":
		#if not the first character check the preceding one and append one char
		#based on this check (no space or two or one consecutive space) to the res var
            if len(res)>0: 	
		if res[-1] != " ":
                    res+=res[-1]+'_'
		    pass	
            else:
           	
		#add underscore at start of string
                res+='_'

		#add _ if in the middle and not double spaces
            else:
		if '  ' in res: 
			if res=='_ ':
                	    res+='_'+'_ '
                	    pass
	            pass
		
        res+=x 
    return res[1:]  
    #return res[1:] is needed if we check the edge case Example   3" with a space or two
    #or not so we return res and no change at all
    
        