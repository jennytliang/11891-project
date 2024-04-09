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
    # 
    txt = txt.replace('\n','').replace('\r','').replace('\t','')
    if len(txt.split()) != 0:
        return txt.split()
    elif len(txt.split(',')) != 0:
        return txt.split(',')
    else:
        return len([i for i in txt if ord(i)%2==1])


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
split_words("abcdef") #, 3
#split_words("abcdefg") #, 4
#split_words("") #, 0
#split_words("a") #, 1
#split_words("bb") #, 2
#split_words("ccc") #, 3
#split_words("ddddd") #, 4
#split_words("eeeeee") #, 5
#split_words("aaaaaa") #, 6
#split_words("zzzzzz") #, 7
#split_words("aaaaa") #, 4
#split_words("bbbbb") #, 5
#split_words("ccccc") #, 6
#split_words("dddddd") #, 7
#split_words("eeeeee") #, 8
#split_words("zzzzzzzz") #, 9
split_words("Hello, world!") #, ["Hello", "world!"]
split_words("Hello,world!") #, ["Hello", "world!"]
split_words("abcdef") #, 3
split_words("abcdefg") #, 4