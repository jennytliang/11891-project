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
    
    if txt.find(' ') != -1:
        return [x.strip() for x in txt.split(' ')]
    elif txt.find(',') != -1:
        return [x.strip() for x in txt.split(',')]
    else:
        return sum([1 for x in txt if ord(x) % 2])
    
    
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
