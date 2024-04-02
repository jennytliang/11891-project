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
    if len(txt.split()) != 0:
        return txt.split()
    if len(txt.split(',')) != 0:
        return txt.split(',')
    else:
        cnt = 0
        for i in range(26):
            if chr(i+ord('a')) in txt:
                cnt += 1
        return cnt
    
    
    
    
split_words("Hello world!")
split_words("Hello,world!")
split_words("abcdef")