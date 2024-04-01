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
	Do not include these tokens in the code: # your code here
	"""
    return 'Yes' if file_name.count('.') == 1 and file_name.count('0') <= 3 and file_name.split('.')[0][0].isalpha() and file_name.split('.')[1] in ['txt','exe','dll'] else 'No'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("smb.1.dll") == "No", "1st example"
    assert file_name_check("a.dll") == "Yes", "2nd example"
    assert file_name_check("ld.exe") == "Yes", "3rd example"
    assert file_name_check("x") == "No", "4th example"
    assert file_name_check("l.b.c") == "No", "5th example"
    assert file_name_check("l.B.c") == "No", "6th example"
    assert file_name_check("smb.1.ar") == "No", "7th example"
    assert file_name_check("smb.ar") == "Yes", "8th example"
