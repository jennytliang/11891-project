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
    whitespace = tuple([' ', '\n', '\r', '\t'])
    if len(set(txt).intersection(whitespace)) == 0:
        return len([x for x in range(len(txt)) if ord(txt[x]) % 2 == 1])
    else:
        return [x for x in txt.split(' ') if len(x) != 0]