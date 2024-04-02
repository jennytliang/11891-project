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
    
	Do not include these tokens in the code: return ' Yes '
	"""
    if file_name.count(".") > 1 or file_name.count(".") == 0:
        return "No"
    elif file_name.count(".") == 1:
        extension = file_name.split(".")[-1]
        if extension in ["txt", "exe", "dll"]:
            if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
                return "No"
            elif file_name.count("0") > 0 or file_name.count("1") > 0 or file_name.count("2") > 0 or file_name.count("3") > 0 or file_name.count("4") > 0 or file_name.count("5") > 0 or file_name.count("6") > 0 or file_name.count("7") > 0 or file_name.count("8") > 0 or file_name.count("9") > 0:
                if file_name[0].isalpha():
                    return "Yes"
                else:
                    return "No"
            elif file_name[0].isalpha():
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("1example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("a1example.exe"))
print(file_name_check("a1example.