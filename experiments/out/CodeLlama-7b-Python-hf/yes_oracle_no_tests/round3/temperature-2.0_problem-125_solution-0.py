def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: (' \
	Do not include these tokens in the code: ([' ', '\
	'''

    whitespace = 0
    comma = 0
    count = 0
    if ' ' in txt:
        whitespace = 1
    elif ',' in txt:
        comma = 1
    else:
        for i in range(len(txt)):
            if ord(txt[i]) % 2 == 1:
                count += 1
    if whitespace == 1:
        return txt.split(' ')
    elif comma == 1:
        return txt.split(',')
    else:
        return count


print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
