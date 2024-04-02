def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: result
	"""

    words = s.split(" " )
    output = " ".join([anti_shuffle_helper(word) for word in words])
    return output

def anti_shuffle_helper(word):
    '''(str) -> str
    Return word with the characters arranged in ascending order.
    '''
    return ''.join(sorted(word))    


print (anti_shuffle_helper("anti_shuffle_helper")) #'ehlloo'
print (anti_shuffle_helper("world")) #'dlrow'

#print (anti_shuffle('Hello World!!!')) #Hello !!!Wdlor

print (anti_shuffle('test'))
print(anti_shuffle('test 123'))

print (anti_shuffle('shall now in due time'))

# edge cases
print (anti_shuffle('')) # ''
print (anti_shuffle('hello')) # 'ehllo'
print (anti_shuffle('Hello')) # 'eHllo'