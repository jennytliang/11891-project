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
#     s=''
#     word=''
#     lst=[]
   
#     for i in txt:
     
#         for j in whitespace:
#             if i==j:
#                 lst.append(word)
#                 word=''
#                 continue
 
#     if word!='':
   
#       lst.append(word)
#     return lst
    
    '''
    Given a string as input, split it as you did before and re-join the string with the words in reverse order.
    Examples
    reverse_split("Hello world!") ➞ "!" world Hello
    reverse_split("Hello,world!") ➞ "!" world Hello
    reverse_split("abcdef") ➞ "fabc"
     
	Include these tokens in the code: delimiter = tuple (', \ n \ r \ t
     
	I suggest you do this by using two loops.
	Also, consider the case that there is no delimiter.
 
     '''
def reverse_split(txt):
    l = txt.split()
    l.reverse()
    ans=''
    for i in l:
        ans+=i + ' '
    ans = ans[:len(ans)-1] 
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert split_words("Hello, world!") == ["Hello", "world!"], "First"
    assert split_words("Hello, , world!") == ["Hello", "", "world!"], "Second"
    assert split_words("  Hello   world   !  ") == ["Hello", "world", "!"], "Third"
    assert reverse_split("Hello world!") == "! world Hello", "First"
    assert reverse_split("Hello, world!") == "! world Hello", "Second"
    assert reverse_split("A brak, jumped over a lazy frog") == "A brak jumped over a lazy frog", "Last"
