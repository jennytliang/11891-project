def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple
	Do not include these tokens in the code: if not txt . count
	'''
 
    if ' ' not in txt and ',' not in txt:
        words = ord(txt[0]) + 1
        for i in range(1,len(txt)):
            if ord(txt[i]) > words:
                words += 1
        return words
            
    return txt.split()
    