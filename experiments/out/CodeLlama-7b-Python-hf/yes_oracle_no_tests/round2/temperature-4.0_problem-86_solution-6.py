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
    
	Do not include these tokens in the code: anti _ sh uff led = [] for
	"""

    words = s.split(" ")[1:]
    anti_shuffle_words = []

    for word in words:
        if word == "":
            anti_shuffle_words.append(word)
        else:
            anti_shuffle_words.append("".join(sorted(word)))

    return " ".join([s.split(" ")[0]] + anti_shuffle_words)
