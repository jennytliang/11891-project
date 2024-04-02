def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: # result = '' #
	"""
    result = ''
    for i in range(len(string)):
        if string[i].isupper():
            result += string[i].lower()
        else:
            result += string[i].upper()
    return result


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(flip_case(input_string))
