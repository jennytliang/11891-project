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
    whitespace_set = list(map(str,whitespace))
    
    text = list(txt)
    if set(text).intersection(set([" ",".","!,",],))== True:
        # for i in text:
        #     if i in whitespace_set:
        #         text.append(" ")
    
    else:
        for i in text:
            if i not in whitespace_set:
                    text.insert(ord(f"a{ord(i) - ord('a')}"),' ')
        
   
    
    return "".join(text).split()
