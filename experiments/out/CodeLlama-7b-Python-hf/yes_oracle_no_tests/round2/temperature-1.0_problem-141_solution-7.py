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
    file_name = file_name.replace(" ", "")
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 1:
        if file_name.count("1") > 2 or file_name.count("2") > 2 or file_name.count("3") > 2 or file_name.count("4") > 2 or file_name.count("5") > 2 or file_name.count("6") > 2 or file_name.count("7") > 2 or file_name.count("8") > 2 or file_name.count("9") > 2:
            return "No"
        if file_name[0].isalpha() == False:
            return "No"
        if file_name[file_name.index(".") + 1] == ".":
            return "No"
        if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
            return "No"
        return "Yes"
    else:
        return "No"

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.exe.exe")) # => 'No' (there should not be more than one dot in the file's name)
print(file_name_check("example.exe.dll")) # => 'No' (there should not be more than one dot in the file's name)
print(file_name_check("1example.txt")) # => 'No' (there should not be more than two digits in the file's name)

def file_name_check_2(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is