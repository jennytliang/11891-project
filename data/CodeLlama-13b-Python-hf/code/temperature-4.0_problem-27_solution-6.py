def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join(x.upper() if x.islower() else x.lower() for x in string)
    
    
    
if __name__ == "__main__":
    input_str = 'Hello World!'
