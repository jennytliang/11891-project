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

 
    # Write your code here.
    import re
    string = file_name
    if(len(string.split(".")) != 2):
        return "No"
    if(re.search(r"[0-9]",string)):
        return "No"
    if(string.split(".")[1] not in ["txt","exe","dll"]):
        return "No"
    if(len(string.split(".")[0]) == 0):
        return "No"
    if(string[0].isalpha() == False):
        return "No"
    return "Yes"


# print(file_name_check("example.txt"))
# print(file_name_check("1example.dll"))
# print(file_name_check("example.txt"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.dll"))
# print(file_name_check("example.doc"))
# print(file_name_check("example.docx"))
# print(file_name_check("example.doxc"))
# print(file_name_check("example.dll"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.txt"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.dll"))
# print(file_name_check("example.doc"))
# print(file_name_check("example.docx"))
# print(file_name_check("example.doxc"))
# print(file_name_check("example.dll"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.txt"))
# print(file_name_check("example.exe"))
# print(file_name_check("example.dll"))
# print(file_name_check("example.doc"))
# print(file_name_check("example.docx"))
# print(file_name_check("example.doxc"))
# print(file_name_check("example.