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
    # first check for the number of dots
    if file_name.count(".") > 1:
        return "No"
    # then find the index of the dot
    dot_index = file_name.index(".")
    # then check the number of digits
    if file_name.count("0") + file_name.count("1") + file_name.count("2") + file_name.count("3") + file_name.count("4") + file_name.count("5") + file_name.count("6") + file_name.count("7") + file_name.count("8") + file_name.count("9") > 3:
        return "No"
    # then check the number of digits
    if file_name.count("0") + file_name.count("1") + file_name.count("2") + file_name.count("3") + file_name.count("4") + file_name.count("5") + file_name.count("6") + file_name.count("7") + file_name.count("8") + file_name.count("9") > 3:
        return "No"
    # then check if the string before the dot is a valid python string
    if len(file_name[:dot_index]) > 0:
        return "No"
    # then check if the string after the dot is a valid python string
    if file_name[dot_index+1:] in ["txt", "exe", "dll"]:
        return "Yes"
    else:
        return "No"


print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example.exe.exe"))  # => 'No' (there should be only one dot)
print(file_name_check("example.dll"))  # => 'Yes'
print(file_name_check