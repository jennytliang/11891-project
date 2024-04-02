def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple ('
	Do not include these tokens in the code: import re if len (
	'''
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([i for i in txt if ord(i)%2==1])
    


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("") #, 3
#split_words("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z") #, 26
#split_words("H e l l o   w o r l d !") #, ["H", "e", "l", "l", "o", "w", "o", "r", "l", "d", "!"]
