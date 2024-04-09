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
    
	Do not include these tokens in the code: # first check for the number of
	"""
    return "Yes" if all([file_name.count(".") == 1, file_name[0].isalpha(), file_name[-4:].lower() in ["txt", "exe", "dll"], file_name.count("0123456789") <= 3]) else "No"


if __name__ == "__main__":
    print(file_name_check("example.txt"))
    print(file_name_check("1example.dll"))
    print(file_name_check("example.exe"))
    print(file_name_check("example.exe.exe"))
    print(file_name_check("example.exe.dll"))
    print(file_name_check("example.dll.exe"))
    print(file_name_check("example.dll.dll"))
    print(file_name_check("example.txt.txt"))
    print(file_name_check("example.exe.txt"))
    print(file_name_check("example.dll.exe.exe"))
    print(file_name_check("example.dll.exe.dll"))
    print(file_name_check("example.dll.dll.exe"))
    print(file_name_check("example.dll.dll.dll"))
    print(file_name_check("example.exe.exe.exe"))
    print(file_name_check("example.exe.exe.dll"))
    print(file_name_check("example.dll.exe.exe.exe"))
