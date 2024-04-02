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
    
	Include these tokens in the code: len ( list ( filter ( lambda ch : ch
	"""

 
    ################################################################################################
    # WRITE YOUR CODE HERE
    # print(len(list(filter(lambda ch: ch.isdigit(), file_name))))
    if len(list(filter(lambda ch: ch.isdigit(), file_name))) > 3:
        return "No"
    elif file_name.find(".") == -1:
        return "No"
    elif file_name[0].isalpha() == False:
        return "No"
    elif file_name[file_name.find(".") + 1:] not in ["txt", "exe", "dll"]:
        return "No"
    else:
        return "Yes"
    
    ################################################################################################
    return "No"

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.py")) # => 'No' (the name should end with one of these: ['txt', 'exe', 'dll'])
print(file_name_check("example.txt.exe.dll")) # => 'No' (the name should have only one dot)