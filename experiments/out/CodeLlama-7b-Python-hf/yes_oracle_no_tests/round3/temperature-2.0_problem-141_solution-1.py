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



    # - There should not be more than three digits ('0'-'9') in the file's name.
    if file_name.count("0") + file_name.count("1") + file_name.count("2") + file_name.count("3") + file_name.count("4") + file_name.count("5") + file_name.count("6") + file_name.count("7") + file_name.count("8") + file_name.count("9") > 3:
        return "No"

    # - The file's name contains exactly one dot '.'
    if file_name.count(".") != 1:
        return "No"

    # - The substring before the dot should not be empty, and it starts with a letter from 
    # the latin alphapet ('a'-'z' and 'A'-'Z').
    if file_name.split(".")[0].strip() == "" or file_name.split(".")[0][0].isdigit():
        return "No"

    # - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    if file_name.split(".")[1] != "txt" and file_name.split(".")[1] != "exe" and file_name.split(".")[1] != "dll":
        return "No"

    return "Yes"
