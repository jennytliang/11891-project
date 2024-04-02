def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace
	Do not include these tokens in the code: # wh ites pace
	'''
    
    if len(txt) == 0:
        return []
    
    if ' ' in txt:
        return txt.split(' ')
    else:
        return [str(sum([((ord(c)%26) + 1) for c in txt if c.isalpha()]))]
