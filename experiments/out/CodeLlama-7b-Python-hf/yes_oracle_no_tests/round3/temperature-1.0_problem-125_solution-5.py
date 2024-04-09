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
    if ' ' in txt:
        return txt.split(' ')
    elif '\n' in txt:
        return txt.split('\n')
    elif '\t' in txt:
        return txt.split('\t')
    elif '\r' in txt:
        return txt.split('\r')
    else:
        return [str(sum(1 for i in range(26) if i % 2 != 0) if txt.islower() else 0)]


print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))