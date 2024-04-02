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
    if s == "":
        return ""
    words = s.split(" ")
    new_words = []
    for word in words:
        if word == "":
            new_words.append("")
        else:
            new_words.append("".join(sorted(word)))
    return " ".join(new_words)


print(anti_shuffle("Hello World!!!"))
print(anti_shuffle("hi"))
print(anti_shuffle(""))
print(anti_shuffle(" "))
print(anti_shuffle("  "))
print(anti_shuffle("  hi"))
print(anti_shuffle("hi  "))
print(anti_shuffle("  hi  "))
print(anti_shuffle("  hi  world"))
print(anti_shuffle("hi  world  "))
print(anti_shuffle("  hi  world  hello"))
print(anti_shuffle("hi  world  hello  "))
print(anti_shuffle("  hi  world  hello  my  name  is  "))
print(anti_shuffle("hi  world  hello  my  name  is   "))
print(anti_shuffle("  hi  world  hello  my  name  is   "))
