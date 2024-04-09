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
	Do not include these tokens in the code: " )[ :: - 1 ] res =
	"""


    words = s.s.split(" ")
    new_words = []
    for word in words:
        new_word = ""
        for char in word:
            new_word += char
        new_words.append(new_word)
    new_words.sort()
    res = ""
    for word in new_words:
        res += word + " "
    return res


if __name__ == "__main__":
    s = "Hello World!!! "
    print(anti_shuffle(s))
