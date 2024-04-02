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
    if len(set(txt)) == 1:
        return ord(txt)
    else:
        return [i for i in txt.split(' ')]


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("abcdef,") #, 3
#split_words("abcdefg") #, 4
#split_words("abcdefg,") #, 4
#split_words("abcdefgh") #, 5
#split_words("abcdefgh,") #, 5
#split_words("abcdefghi") #, 6
#split_words("abcdefghi,") #, 6
#split_words("abcdefghij") #, 7
