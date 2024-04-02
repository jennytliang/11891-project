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
        return []
    if len(txt) == 1:
        return [txt]
    if len(txt) == 2:
        return [txt]
    if ' ' in txt:
        return txt.split()
    if ', ' in txt:
        return txt.split(', ')
    else:
        cnt = 0
        for i in range(26):
            if ord(chr(ord('a') + i)) % 2 == 1:
                cnt += 1
        return cnt
    
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words("a"))
print(split_words(""))
print(split_words("b"))
print(split_words("c"))
print(split_words("ab"))
print(split_words("abc"))
print(split_words("abcd"))
print(split_words("abcde"))
print(split_words("abcdef"))
print(split_words("abcdefg"))
print(split_words("abcdefgh"))
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
print(split_words("abcdefghijklmnop