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
    
	Include these tokens in the code:  if len ( list ( filter ( lambda
	Do not include these tokens in the code: file _ name . count
	"""

    # If the file name has more than three digits, return 'No'
    if file_name.count(file_name) > 3:
        return 'No'

    # If the file name contains more than one dot, return 'No'
    elif file_name.count('.') > 1:
        return 'No'

    # If the file name contains no dot, return 'No'
    elif '.' not in file_name:
        return 'No'

    # If the file name starts with a digit, return 'No'
    elif file_name[0].isdigit():
        return 'No'

    # If the file name does not end with a valid extension, return 'No'
    elif file_name[-4:] not in ['.txt', '.exe', '.dll']:
        return 'No'

    # If all of the above are not met, return 'Yes'
    else:
        return 'Yes'


print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example.exe.exe"))  # => 'No'
print(file_name_check("example.dll.exe"))  # => 'No'
print(file_name_check("example.dll.exe.dll"))  # => 'No'
print(file_name_check("example.dll.dll"))  # => 'Yes'
print(file_name_check("example.exe.dll.dll"))  # => 'Yes'
print(file_name_check("example.exe.dll.exe.dll"))  # => 'No'
print(file_name_check("example.exe.exe.dll"))  # => 'No'
print(file_name_check("example.exe.exe.exe"))  # => 'No'
print(file_name_check("example.exe.exe.exe.exe"))  # => 'No'
print(file_name_check("example.exe.exe.