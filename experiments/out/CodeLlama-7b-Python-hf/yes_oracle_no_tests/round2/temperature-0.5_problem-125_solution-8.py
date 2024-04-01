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
    
    # check if there are whitespaces
    if ' ' in txt:
        # split on whitespaces
        return txt.split(' ')
    # check if there are commas
    elif ',' in txt:
        # split on commas
        return txt.split(',')
    # if there are no whitespaces or commas, return the number of lower-case letters with odd order in the alphabet
    else:
        # get the number of lower-case letters with odd order in the alphabet
        return len([i for i in range(26) if ord('a')+i%2 == ord(txt)])
        