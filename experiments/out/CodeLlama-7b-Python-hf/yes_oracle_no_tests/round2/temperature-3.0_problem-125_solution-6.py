def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace
	Do not include these tokens in the code: txt
	'''
    if txt.find(" ") != -1:
        return txt.split(" ")
    if txt.find(",") != -1:
        return txt.split(",")
    else:
        count = 0
        for i in range(len(txt)):
            if ord(txt[i])%2 != 0:
                count += 1
        return count
    
    
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words(" "))
print(split_words("a"))
print(split_words("abc"))
print(split_words("abc,def"))
print(split_words("abc,def,ghi"))
print(split_words("abc,def,ghi,jkl"))
print(split_words("abc,def,ghi,jkl,mno"))
print(split_words("abc,def,ghi,jkl,mno,pqr"))
print(split_words("abc,def,ghi,jkl,mno,pqr,stu"))
print(split_words("abc,def,ghi,jkl,mno,pqr,stu,vwx"))
print(split_words("abc,def,ghi,jkl,mno,pqr,stu,vwx,yz"))