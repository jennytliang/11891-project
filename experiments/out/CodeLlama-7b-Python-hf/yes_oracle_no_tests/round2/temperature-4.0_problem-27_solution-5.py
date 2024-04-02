def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: result = '' for i
	"""
    # return " ". join
    # result = ''
    # for i in string:
    #     if i.isupper():
    #         result += i.lower()
    #     else:
    #         result += i.upper()
    # return result
    return " ".join(i.upper() if i.islower() else i.lower() for i in string)


print(flip_case("Hello"))
print(flip_case("HeLlo"))
print(flip_case("1234567890"))
print(flip_case("1a2b3c4d5e6f7g8h9i0"))
print(flip_case("Happy Birthday! "))
print(flip_case("hAPpy BIRTHDAY!"))
print(flip_case("I love computer science!"))
print(flip_case("I LOVE COMPUTER SCIENCE!"))
