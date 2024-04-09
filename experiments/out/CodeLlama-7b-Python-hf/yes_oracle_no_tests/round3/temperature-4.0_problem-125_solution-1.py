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
    else:
        if ' ' in txt:
            return txt.split(' ')
        elif ',' in txt:
            return txt.split(',')
        else:
            return [str(len([i for i in range(26) if ord('a') + i%2 == ord(txt[i])]))]
    

split_words("Hello world!") #, ["Hello", "world!"]
split_words("Hello,world!") #, ["Hello", "world!"]
split_words("abcdef") #, 3
split_words("") #, []