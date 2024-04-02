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
    # your code here
    if not txt.find(' ') == -1:
        return txt.split()
    elif not txt.find(',') == -1:
        return txt.split(',')
    else:
        return len([i for i in range(26) if ord(chr(i+97)) % 2 == 1])


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("a,b,c,d,e,f") #, ["a", "b", "c", "d", "e", "f"]
#split_words("") #, 3
#split_words("abcde") #, 4
#split_words("abcdefghijklmnopqrstuvwxyz") #, 3
#split_words("abcdefghijklmnopqrstuvwxyza") #, 4
