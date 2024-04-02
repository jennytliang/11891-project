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
    
    if not txt.count(' ') or not txt.count(','):
        txt2 = ['' for i in range(26)]
        ind = ord('a')
        cind = 0
        for i in txt:
            txt2[cind] = list(txt2[cind])
            if i ==",":
                ind = ord('a')
                cind +=1
                continue
            if ord(i)>=ord('a') and ord(i)<=ord('z'):
                txt2[cind] += chr(ind)
                ind += 1
                
        return sum([i.count("a") for i in txt2])
    whsp = (" \n\r\t")
    whsp2= txt.split(whsp)
    return [i for i in whsp2]


print(split_words("Hello,world!"))