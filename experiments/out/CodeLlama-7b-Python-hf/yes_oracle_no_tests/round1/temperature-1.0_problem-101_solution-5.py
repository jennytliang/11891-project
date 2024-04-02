def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    ##############################
    ## INSERT YOUR CODE HERE
    import re
    res = re.split (" |,",s)
    #remove leading empty spaces, and last one if exist
    res = [r for r in res if len(r)<len(r.lstrip()) and len(r)>0]
    return res
    ##############################
    return []
       