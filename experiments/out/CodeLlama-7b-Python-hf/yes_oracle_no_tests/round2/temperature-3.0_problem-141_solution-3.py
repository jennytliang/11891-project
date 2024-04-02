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
    
	Do not include these tokens in the code: # Your code here #
	"""
    # Your code here
    import re
    if file_name.count(".") != 1:
        return "No"
    if file_name.count(" ") != 0:
        return "No"
    if file_name.count("0") > 2 or file_name.count("1") > 2 or file_name.count("2") > 2 or file_name.count("3") > 2 or file_name.count("4") > 2 or file_name.count("5") > 2 or file_name.count("6") > 2 or file_name.count("7") > 2 or file_name.count("8") > 2 or file_name.count("9") > 2:
        return "No"
    if not re.search(r"[a-zA-Z]", file_name):
        return "No"
    if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("e.txt"))
print(file_name_check("e.exe"))
print(file_name_check("e.dll"))
print(file_name_check("e.exe.txt"))
print(file_name_check("e.exe.exe"))
print(file_name_check("e.exe.dll"))
print(file_name_check("e.txt.exe"))
print(file_name_check("e.txt.dll"))
print(file_name_check("e.dll.exe"))
print(file_name_check("e.dll.dll"))
print(file_name_check("e.exe.exe.txt"))
print(file_name_check("e.exe.exe.exe"))
print(file_name_check("e.exe.exe.dll"))
print(file_name_check("e.exe.txt.exe"))
print(file_name_check("e.exe.txt.dll