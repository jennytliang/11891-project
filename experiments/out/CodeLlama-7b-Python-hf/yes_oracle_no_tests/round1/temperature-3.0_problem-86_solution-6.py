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
    
    # Your code goes here
    words = s.split(" ")
    result = ""
    for word in words:
        if word == "":
            result += " "
        else:
            letters = list(word)
            letters.sort()
            result += "".join(letters)
            result += " "
    return result[:-1]


if __name__ == "__main__":
    print(anti_shuffle("Hello world!!! "))
    print(anti_shuffle("Hi"))
    print(anti_shuffle(""))
    print(anti_shuffle(" "))
    print(anti_shuffle("Hello world"))
    print(anti_shuffle("Hello   world"))
    print(anti_shuffle("Hello   world     "))
    print(anti_shuffle("Hello   world     Hello"))
    print(anti_shuffle("Hello   world     Hello    "))
    print(anti_shuffle("Hello   world     Hello    Hi"))
