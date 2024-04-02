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
    
	Include these tokens in the code: words = s . split (" ")
	"""
    words = s.split(" ")
    
    # print(words)

    anti_shuffled_string = " "
    for word in words:
        letter = ""
        
        if word == "":
            anti_shuffled_string += " "
        else:
            for letter in word:
                anti_shuffled_string += sorted(letter)[0]

            anti_shuffled_string += " "

    return anti_shuffled_string[:-1]


print(anti_shuffle('Hi'))
print(anti_shuffle('hello'))
print(anti_shuffle('Hello World!!!'))
