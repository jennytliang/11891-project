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
    if len(txt) == 0:
        return txt
    if txt.find(' ') != -1:
        return txt.split(' ')
    elif txt.find(',') != -1:
        return txt.split(',')
    else:
        return len([x for x in txt if ord('a') <= ord(x) <= ord('z') and ord(x) % 2 == 1])


print(split_words("Hello, world!"))
print(split_words("Hello world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words("abc"))
print(split_words("Abc"))
print(split_words("123"))
print(split_words("abcdef"))
print(split_words("abcdefg"))
print(split_words("abcdefghi"))
print(split_words("abcdefghij"))
print(split_words("abcdefghijk"))
print(split_words("abcdefghijkl"))
print(split_words("abcdefghijklm"))
print(split_words("abcdefghijklmn"))
print(split_words("abcdefghijklmno"))
print(split_words("abcdefghijklmnop"))
print(split_words("abcdefghijklmnopq"))
print(split_words("abcdefghijklmnopqr"))
print(split_words("abcdefghijklmnopqrs"))
print(split_words("abcdefghijklmnopqrst"))
print(split_words("abcdefghijklmnopqrstu"))
print(split_words("abcdefghijklmnopqrstuv"))
print(split_words("abcdefghijklmnopqrstuvw"))
print(split_words("abcdefghijklmnopqrstuvwx"))
print(split_words("abcdefghijklmnopqrstuvwxy"))
print(split_words("abcdefghijklmnopqrstuvwxyz"))
print(split_words("abcdefghijklmnopqr