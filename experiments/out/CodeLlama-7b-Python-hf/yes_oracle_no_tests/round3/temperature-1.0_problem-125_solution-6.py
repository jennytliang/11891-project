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
    
    txt = txt.replace('\n','').replace('\r','').replace('\t','').replace(',','').replace(' ','')
    if len(txt) == 0:
        return []
    return list(txt)
    


#split_words("Hello world!") #➞ ["Hello", "world!"]
#split_words("Hello,world!") #➞ ["Hello", "world!"]
#split_words("abcdef") == 3 
#split_words("") == []
#split_words("abc") == 3
#split_words("abc,def") == 3
#split_words("abc,def,") == 3
#split_words("abc,def,gh") == 3
#split_words("abc,def,gh,") == 3
#split_words("abc,def,gh,ij") == 3
#split_words("abc,def,gh,ij,") == 3
#split_words("abc,def,gh,ij,kl") == 3
#split_words("abc,def,gh,ij,kl,") == 3
#split_words("abc,def,gh,ij,kl,mn") == 3
#split_words("abc,def,gh,ij,kl,mn,") == 3
#split_words("abc,def,gh,ij,kl,mn,op") == 3
#split_words("abc,def,gh,ij,kl,mn,op,") == 3
#split_words("abc,def,gh,ij,kl,mn,op,qr") == 3
#split_words("abc,def,gh,ij,kl,mn,op,qr,") == 3
#split_words("abc,def,gh,ij,kl,mn,op,qr,st") == 3
#split_words("abc,def,gh,ij,kl,mn,op,qr,st,") == 3
#split_words("abc,def,gh,ij,kl,mn,op,qr,st,uv") == 3
#split_words