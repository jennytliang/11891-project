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
	Do not include these tokens in the code: # Your code here
	"""
    return "No"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("example.txt") == "Yes", "First"
    assert file_name_check("asdf.exe") == "Yes", "Second"
    assert file_name_check("Not e.Xe") == "No", "Third"
    assert file_name_check(" a.txt") == "No", "Four"
    assert file_name_check("e0.txt") == "No", "Fifth"
    assert file_name_check("e.txt.") == "No", "Six"
    assert file_name_check("e.t") == "No", "Seventh"
    assert file_name_check("e.tx") == "No", "Eighth"
    assert file_name_check("e.txtt") == "No", "Ninth"
    assert file_name_check("e.tx.tx") == "No", "Tenth"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
