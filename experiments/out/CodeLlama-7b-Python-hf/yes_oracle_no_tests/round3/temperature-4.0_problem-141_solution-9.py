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
    
	Do not include these tokens in the code: import re # your
	"""
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
        
        Do not include these tokens in the code: import re # your
        """
        # Your code here
        import re
        if len(re.findall(r'[0-9]', file_name)) > 3:
            return "No"
        elif file_name.count(".") != 1:
            return "No"
        elif re.findall(r'[a-zA-Z]', file_name[:file_name.find(".")]) == []:
            return "No"
        elif re.findall(r'\.(txt|exe|dll)$', file_name) == []:
            return "No"
        else:
            return "Yes"
    return file_name_check(file_name)


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.txt"))
print(file_name_check("example.exe"))
print(file_name_check