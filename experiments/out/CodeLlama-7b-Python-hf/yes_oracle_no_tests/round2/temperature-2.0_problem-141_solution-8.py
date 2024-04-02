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
    
	Do not include these tokens in the code: # Your code here import
	"""
    # Your code here
    return "Yes" if (file_name.count(".") == 1 and file_name.find(".") != 0 and file_name.find(" ") == -1 and file_name.find("0") == -1 and file_name.find("1") == -1 and file_name.find("2") == -1 and file_name.find("3") == -1 and file_name.find("4") == -1 and file_name.find("5") == -1 and file_name.find("6") == -1 and file_name.find("7") == -1 and file_name.find("8") == -1 and file_name.find("9") == -1 and file_name[0].isalpha() and file_name.find("txt") != -1 or file_name.find("exe") != -1 or file_name.find("dll") != -1) else "No"


def file_name_check_2(filename):
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
    
	Do not include these tokens in the code: # Your code here import
	"""
    # Your code here
    return "Yes" if (filename.count(".") == 1 and filename