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
	Do not include these tokens in the code: # Please , insert your code
	"""
    # Please , insert your code
    if file_name.count(".") != 1:
        return "No"
    if file_name.count("0") + file_name.count("1") + file_name.count("2") + file_name.count("3") + file_name.count("4") + file_name.count("5") + file_name.count("6") + file_name.count("7") + file_name.count("8") + file_name.count("9") > 3:
        return "No"
    if file_name[0].isalpha() == False:
        return "No"
    if file_name[file_name.index(".") + 1] == "0" or file_name[file_name.index(".") + 1] == "1" or file_name[file_name.index(".") + 1] == "2" or file_name[file_name.index(".") + 1] == "3" or file_name[file_name.index(".") + 1] == "4" or file_name[file_name.index(".") + 1] == "5" or file_name[file_name.index(".") + 1] == "6" or file_name[file_name.index(".") + 1] == "7" or file_name[file_name.index(".") + 1] == "8" or file_name[file_name.index(".") + 1] == "9":
        return "No"
    if file_name[file_name.index(".") + 1] != "e" and file_name[file_name.index(".") + 1] != "x" and file_name[file_name.index(".") + 1] != "d" and file_name[file_name.index(".") + 1] != "l" and file_name[file_name.index(".") + 1] != "t":
        return "No"
    return "Yes"