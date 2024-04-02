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
        if txt.isalpha():
            return [txt]
        elif txt.isnumeric():
            return [txt]
        elif txt in ['\n', '\r', '\r\n', '\n\r', '\t']:
            return [txt]
        else:
            return [txt]
    
    elif len(txt) > 1:
        if txt.isalpha():
            return [txt]
        elif txt.isnumeric():
            return [txt]
        elif txt.isalnum():
            return [txt]
        else:
            return [txt]

    else:
        return []



def split_words(txt):
    if txt == "":
        return []
    elif txt.isalpha():
        return [txt]
    elif txt.isnumeric():
        return [txt]
    elif txt.isalnum():
        return [txt]
    else:
        return [txt]



#split_words("Hello world!") #➞ ["Hello", "world!"]
#split_words("Hello,world!") #➞ ["Hello", "world!"]
#split_words("abcdef") #== 3
#split_words("") #== []
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_words("abcdef") #== [abcdef]
#split_