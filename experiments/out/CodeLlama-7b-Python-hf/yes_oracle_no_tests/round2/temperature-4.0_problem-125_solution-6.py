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
    for i in txt:
        if i in whitespace:
            txt = txt.split()
    if not whitespace in txt:
        txt = sum([1 for i in txt if ord(i) % 2])
    return txt


txt = "the quick brown fox jumps over the lazy dog"
print(split_words(txt))