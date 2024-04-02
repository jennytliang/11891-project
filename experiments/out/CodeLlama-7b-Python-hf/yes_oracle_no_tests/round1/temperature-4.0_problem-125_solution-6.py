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
    
    if not txt:
        return []
    elif txt.isalpha():
        return [txt]
    elif ' ' in txt:
        return txt.split()
    elif ', ' in txt:
        return txt.split(', ')
    else:
        return [txt]
    


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("") #, []
#split_words("a") #, ["a"]
#split_words("Hello, world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world") #, ["Hello", "world"]
#split_words("Hello, world") #, ["Hello", "world"]
#split_words("Hello") #, ["Hello"]
#split_words("a, b") #, ["a", "b"]
#split_words("a,b") #, ["a", "b"]
#split_words("a, b, c") #, ["a", "b", "c"]
#split_words("a,b,c") #, ["a", "b", "c"]
#split_words("a,,b,c") #, ["a", "", "b", "c"]
#split_words("a,b,c,") #, ["a", "b", "c", ""]
#split_words("a,b,c,d") #, ["a", "b", "c", "d"]
#split_words("a") #, ["a"]
#split_words("") #, []
