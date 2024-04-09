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
    
	Include these tokens in the code: ")
	Do not include these tokens in the code: " )[ :: - 1 ] print (
	"""


    words = s.s.split(" ")
    output = ""

    for word in words:
        char_list = list(word)
        char_list.sort()
        output += "".join(char_list) + " "

    return output[:-1]


print(anti_shuffle("Hello World!!!"))
