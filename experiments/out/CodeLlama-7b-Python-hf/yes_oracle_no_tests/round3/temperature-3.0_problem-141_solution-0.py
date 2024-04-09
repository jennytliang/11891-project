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
    count_no_digits = 0
    count_dots = 0
    for ch in file_name:
        if ch.isdigit():
            count_no_digits += 1
        if ch == '.':
            count_dots += 1
    if count_no_digits <= 3 and count_dots == 1:
        if file_name.startswith(('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z')):
            if file_name[-4:] in ['.txt', '.exe', '.dll']:
                return 'Yes'
    return 'No'


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.py"))
print(file_name_check("example"))
print(file_name_check("example.123"))
print(file_name_check("example.123.exe"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.dll.exe.exe"))
print(file_name_check("example.dll.dll.exe"))
print(file_name_check("example.exe.exe.exe"))
