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
	Do not include these tokens in the code: count = 0 ;
	"""
    if file_name == "":
        return ("No")
    if file_name.count(".") != 1:
        return ("No")

    dot = file_name.index(r".")
    file_name = file_name[:dot]
    if int(file_name.isdigit) == 1:
        return ("No")
    if file_name[0].isalpha() == False:
        return ("No")
    else:
        file_name = file_name[1:]
        for i in range(len(file_name)):
            if file_name[i].isalpha == False:
                return ("No")
    if file_name.endswith("txt") == True or file_name.endswith("exe") == True or file_name.endswith(
            "dll") == True:
        return ("Yes")
    else:
        return ("No")


print(file_name_check("example.txt"))
