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
    if len(txt)==0:
        return []
    if ' ' not in txt and ',' not in txt:
        return len([i for i in txt if ord(i)>=ord('a') and ord(i)<=ord('z') and ord(i)%2==1])
    else:
        return txt.split()


split_words('Hello world!') #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
split_words("abcdef") #, 3
split_words("") #, []
split_words("Hello,world!") #, ["Hello", "world!"]
split_words("Hello world") #, ["Hello", "world"]
split_words("aAbBcC") #, 3
split_words("aAbBcC,") #, ["aAbBcC", ""]
split_words("aAbBcCdE") #, 5
split_words("aAbBcCdEf") #, 5
split_words("aAbBcCdEf,") #, ["aAbBcCdEf", ""]
split_words("aAbBcCdEf,g") #, ["aAbBcCdEf", "g"]
split_words("aAbBcCdEf,g,") #, ["aAbBcCdEf", "g", ""]
split_words("aAbBcCdEf,g,h") #, ["aAbBcCdEf", "g", "h"]
split_words("aAbBcCdEf,g,h,") #, ["aAbBcCdEf", "g", "h", ""]
split_words("aAbBcCdEf,g,h,i") #, ["aAbBcCdEf", "g", "h", "i"]
