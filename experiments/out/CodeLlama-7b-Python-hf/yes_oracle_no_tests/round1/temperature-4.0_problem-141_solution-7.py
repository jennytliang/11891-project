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
    # write your code here
    # get the index of the dot
    dot_index = file_name.index(".")
    # get the substring before the dot
    substring_before_dot = file_name[:dot_index]
    # get the substring after the dot
    substring_after_dot = file_name[dot_index + 1:]
    # check if the substring before the dot contains a digit
    if any(map(str.isdigit, substring_before_dot)):
        return "No"
    # check if the substring before the dot starts with a letter
    if substring_before_dot[0].isalpha():
        return "No"
    # check if the substring after the dot is one of the following: ['txt', 'exe', 'dll']
    if any(substring_after_dot == x for x in ["txt", "exe", "dll"]):
        return "Yes"
    else:
        return "No"


# print(file_name_check("example.txt"))
# print(file_name_check("1example.dll"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.exe.exe"))
# print(file_name_check("example.exe.dll"))
# print(file_name_check("example.dll.exe"))
# print(file_name_check("example.txt.txt"))
# print(file_name_check("example.txt.dll"))
# print(file_name_check("example.dll.txt"))
