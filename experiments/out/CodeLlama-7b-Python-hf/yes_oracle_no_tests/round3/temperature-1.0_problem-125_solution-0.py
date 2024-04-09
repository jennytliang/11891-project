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
    # Your code here
    import string
    l = len(txt)
    txt = txt.strip()
    if txt == '':
        return []
    elif len(txt) == 1:
        return txt
    elif len(txt) > 1 and txt.isalpha():
        odd = []
        for x in range(l):
            if ord(txt[x]) % 2 == 1:
                odd.append(txt[x])
        return odd
    else:
        return txt.split()
