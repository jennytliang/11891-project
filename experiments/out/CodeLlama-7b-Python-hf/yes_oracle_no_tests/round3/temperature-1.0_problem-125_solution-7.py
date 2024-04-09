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
    for i in txt:
        if i in whitespace:
            return txt.split()
    return len([i for i in txt if ord(i)%2==1])


#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("abc") #, 2
#split_words("a") #, 1
#split_words("") #, 0
#split_words("abcdefghijklmnopqrstuvwxyz") #, 25
#split_words("abcdefghijklmnopqrstuvwxyza") #, 26
#split_words("abcdefghijklmnopqrstuvwxyz,") #, 26
#split_words("abcdefghijklmnopqrstuvwxyz ") #, 26
#split_words("abcdefghijklmnopqrstuvwxyz!") #, 26
#split_words("abcdefghijklmnopqrstuvwxyz?") #, 26



def fizz_buzz(n):
    '''
    Return a list containing the numbers from one to n, but if the number is divisible by 3 say "fizz",
    if the number is divisible by 5, say "buzz", if the number is divisible by both 3 and 5, say "fizzbuzz"
    Examples
    fizz_buzz(15) ➞ ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
    fizz_buzz(10) ➞ ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]
    fizz_buzz(2