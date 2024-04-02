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
    count_digit = 0
    for ch in file_name:
        if ch.isdigit():
            count_digit += 1
            if count_digit > 3:
                return "No"
    count_dot = 0
    for ch in file_name:
        if ch == ".":
            count_dot += 1
            if count_dot > 1:
                return "No"
    if count_dot != 1:
        return "No"
    if file_name[0].isdigit():
        return "No"
    if file_name[0].isalpha() == False:
        return "No"
    if file_name[file_name.find(".")+1:].lower() not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"


print(file_name_check("example.txt"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe1"))
