def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple ('
	Do not include these tokens in the code: if any ( c in
	'''
    
    if len(txt.split()) > 0: return txt.split()
    elif len(txt.split(',')) > 0: return txt.split(',')   
    else:
        words = 0 
        for w in txt:
            if ord(w) > 96 and ord(w) < 122:
                if ord(w) % 2 != 0 and ord(w) % 1 == 0:
                    words +=1
        return words