def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for char in string:
        if char.isupper():
            ret += char.lower()
        elif char.islower():
            ret += char.upper()
        else:
            ret += char
    return ret


print(flip_case("Hello"))
print(flip_case("Bye"))
print(flip_case("Hello"))
print(flip_case("Bye"))

# Study Drills
# 1. Try to write a different version of this that uses nested ifs instead of
#    the or operator. Do you like it better?
# A: No, it is harder to read.

# 2. Find a word with at least 10 letters in the dictionary file and try to
#    use it.
# A: I like 'ultracentrifugation'.

# 3. Fill in the functions argument so the code runs and prints out the expected
#    output.
# A:
# print(flip_case("I love programming."))
# print(flip_case("I love candy."))
# print(flip_case("I love cake."))

# 4. Go back through your program and write a comment on what each line does.
# A:
# flip_case(string: str) -> str:
#     ret = ""
#     for char in string:
#         if char.isupper():
#             ret += char.lower()
#         elif char.islower():
#             ret += char.upper()
#         else:
#             ret += char
#     return ret

# 5. Figure out how to make this code faster. Hint: Look into timeit.
# A: I tried to use the timeit module, but I couldn't figure out how to make it work.