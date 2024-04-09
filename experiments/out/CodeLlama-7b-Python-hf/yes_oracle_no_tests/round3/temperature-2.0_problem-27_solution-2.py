def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	"""
    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


# strings_to_flip = [
#     "Hello",
#     "goodbye",
#     "I am on my way",
#     "Hasta la vista",
#     "",
#     "12345",
#     "1a2b3c4d5e",
# ]
# for string in strings_to_flip:
#     print(string)
#     print(flip_case(string))
#     print("")
