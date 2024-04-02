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
    # s = s.split(" ")
    # new_string = ""
    # for i in range(len(s)):
    #     if s[i] == "":
    #         new_string += " "
    #     else:
    #         s[i] = sorted(s[i])
    #         new_string += "".join(s[i]) + " "
    # return new_string.strip()
    return " ".join(["".join(sorted(w)) for w in s.split(" ") if w != ""])


print(anti_shuffle("Hello World!!!"))
print(anti_shuffle("Hi"))
print(anti_shuffle("hello"))
