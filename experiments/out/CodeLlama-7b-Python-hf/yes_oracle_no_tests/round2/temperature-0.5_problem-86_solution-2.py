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
    
	Do not include these tokens in the code: if len ( s ) ==
	"""
    
    # Initialization
    new_s = ''
    word_count = 0
    word_list = s.split()
    
    # Loop through the word list
    for word in word_list:
        if word == '':
            new_s += ' '
        else:
            word_count += 1
            new_word = ''.join(sorted(word))
            new_s += new_word
            if word_count != len(word_list):
                new_s += ' '
    
    return new_s

# Test cases
print anti_shuffle('Hi')
print anti_shuffle('hello')
print anti_shuffle('Hello World!!!')
print anti_shuffle('')
print anti_shuffle('    ')
print anti_shuffle('    Hello World!!!   ')
