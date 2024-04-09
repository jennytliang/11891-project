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
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 0:
        return "No"
    if file_name.count(".") == 1:
        if file_name.index(".") == 0:
            return "No"
        if file_name.index(".") == len(file_name) - 4:
            return "No"
        if file_name.index(".") == len(file_name) - 5:
            return "No"
        if file_name.index(".") == len(file_name) - 6:
            return "No"
        if file_name.index(".") == len(file_name) - 7:
            return "No"
        if file_name.count("0") > 3:
            return "No"
        if file_name.count("1") > 3:
            return "No"
        if file_name.count("2") > 3:
            return "No"
        if file_name.count("3") > 3:
            return "No"
        if file_name.count("4") > 3:
            return "No"
        if file_name.count("5") > 3:
            return "No"
        if file_name.count("6") > 3:
            return "No"
        if file_name.count("7") > 3:
            return "No"
        if file_name.count("8") > 3:
            return "No"
        if file_name.count("9") > 3:
            return "No"
        if file_name.index(".") < file_name.index("."):
            return "No"
        if file_name[0].isdigit():
            return "No"
        if file_name[file_name.index(".") + 1] == "0":
            return "No"
        if file_name[file_name.index(".") + 1] == "1":
            return "No"
        if file_name[file_name