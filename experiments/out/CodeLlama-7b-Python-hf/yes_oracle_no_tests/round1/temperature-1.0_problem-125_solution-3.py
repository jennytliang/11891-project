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
    #whitespace = (' ', '\n', '\r', '\t')
    #split_text = []
    #for i in txt:
    #    if i in whitespace:
    #        split_text.append(i)
    #return split_text
    if ' ' in txt:
        return txt.split(' ')
    elif '\n' in txt:
        return txt.split('\n')
    elif '\r' in txt:
        return txt.split('\r')
    elif '\t' in txt:
        return txt.split('\t')
    else:
        return len([i for i in txt if ord(i)%2==1])
    
    
    

split_words("Hello world!") #, ["Hello", "world!"])
#split_words("Hello,world!") #, ["Hello", "world!"])
#split_words("abcdef") #, 3)
#split_words("abcdefg") #, 5)
#split_words("abcdefgh") #, 7)
#split_words("abcdefghij") #, 9)
#split_words("abcdefghijkl") #, 11)
#split_words("abcdefghijklmn") #, 13)
#split_words("abcdefghijklmnop") #, 15)
#split_words("abcdefghijklmnopq") #, 17)
#split_words("abcdefghijklmnopqr") #, 19)
#split_words("abcdefghijklmnopqrs") #, 21)
#split_words("abcdefghijklmnopqrst") #, 23)