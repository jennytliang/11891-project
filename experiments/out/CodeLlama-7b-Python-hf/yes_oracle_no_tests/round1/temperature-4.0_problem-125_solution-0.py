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
    if len(txt) == 0: return []
    if len(txt) == 1:
        if ord(txt) in range(ord('a'), ord('z') + 1):
            return ord(txt) % 2
        else: return txt
    if len(txt) == 2:
        return ord(txt) % 2
    
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return [ord(txt) % 2]
    
#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("abcdefg") #, 4
#split_words("abcde") #, 1
#split_words("a") #, 1
#split_words("") #, []
#split_words("hello") #, 1
#split_words("hello,world") #, ["hello", "world"]
#split_words("hello world") #, ["hello", "world"]
#split_words("hello,world") #, ["hello", "world"]
#split_words("hello, world") #, ["hello", "world"]
#split_words("hello,world") #, ["hello", "world"]
#split_words("hello, world") #, ["hello", "world"]
#split_words("hello world!") #, ["hello", "world!"]
#split_words("hello,world!") #, ["hello", "world!"]
#split_words("hello, world!") #, ["hello", "world!"]
#split_words("hello world!") #, ["hello", "world!"]
#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("Hello, world!") #, ["Hello", "world!"]
#split_words("Hello world!