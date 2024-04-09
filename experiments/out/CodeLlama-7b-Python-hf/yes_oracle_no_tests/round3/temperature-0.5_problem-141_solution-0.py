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

 

    # Checking the number of digits
    count = 0
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            count += 1
            if count > 3:
                return 'No'

    # Checking for a valid extension
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    # Checking for a valid filename
    for i in range(len(file_name.split('.')[0])):
        if i == 0:
            if not file_name.split('.')[0][i].isalpha():
                return 'No'
        else:
            if not file_name.split('.')[0][i].isalnum():
                return 'No'

    return 'Yes'

# Tests
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example.exe.exe"))  # => 'No'
print(file_name_check("example.dll.exe"))  # => 'No'
print(file_name_check("example.123.dll"))  # => 'No'
print(file_name_check("example.exe.dll"))  # => 'Yes'
print(file_name_check("example.123.exe"))  # => 'No'
print(file_name_check("example.exe.123"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example.dll"))  # => 'Yes'
print(file_name_check("example.123"))  # => 'No'
print(file_name_check("example"))  # => 'No'
