def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple (' \ n \ r \ t
	'''
    
    
    if len(txt) == 0:
        return []
    elif len(txt) == 1:
        return [txt]
    elif len(txt) == 2:
        if txt[0] == txt[1]:
            return [txt]
        else:
            return [txt[0], txt[1]]
    
    if len(txt) > 0:
        if len(txt) > 1:
            if txt[0] == txt[1]:
                return [txt[0], split_words(txt[2:])]
            else:
                return [txt[0], split_words(txt[1:])]
        else:
            return [txt]
    
    
        
        


def split_words(txt):
    if len(txt) == 0:
        return []
    elif len(txt) == 1:
        return [txt]
    elif len(txt) == 2:
        if txt[0] == txt[1]:
            return [txt]
        else:
            return [txt[0], txt[1]]
    
    if len(txt) > 0:
        if len(txt) > 1:
            if txt[0] == txt[1]:
                return [txt[0], split_words(txt[2:])]
            else:
                return [txt[0], split_words(txt[1:])]
        else:
            return [txt]
    
    
    
    

def split_words(txt):
    if len(txt) == 0:
        return []
    elif len(txt) == 1:
        return [txt]
    elif len(txt) == 2:
        if txt[0] == txt[1]:
            return [txt]
        else:
            return [txt[0], txt[1]]
    
    if len(txt) > 0:
        if len(txt) > 1:
            if txt[0] == txt[1]:
                return [txt[0], split_words(txt[2:])]
            else:
