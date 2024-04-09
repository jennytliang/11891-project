def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    
	Include these tokens in the code: if len ( list ( filter ( lambda ch :
	"""
    # Your code here
    from re import search
    return 'Yes' if search('^[a-zA-Z][a-zA-Z0-9]{0,2}\.[a-zA-Z0-9]{3}$', file_name) else 'No'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("example.txt") == "Yes", "First"
    assert file_name_check("example.dll") == "Yes", "Second"
    assert file_name_check("example.exe") == "Yes", "Third"
    assert file_name_check("WebSite.com") == "No", "Fourth"
    assert file_name_check("Start.HTML") == "No", "Fifth"
    assert file_name_check("o.txt") == "No", "Sixth"
    assert file_name_check("Web.HTML.zip") == "No", "Seventh"
    assert file_name_check("Web.") == "No", "Eight"
    assert file_name_check("1.txt") == "No", "Ninth"
    assert file_name_check("Web 2 HTML") == "No", "Tenth"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")