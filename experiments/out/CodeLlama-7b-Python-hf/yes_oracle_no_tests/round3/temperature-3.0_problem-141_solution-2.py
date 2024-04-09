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
	Do not include these tokens in the code: # My solution
	"""
    if file_name.count(".") == 1 and file_name.count(" ") == 0:
        if file_name.count("0") <= 1 and file_name.count("1") <= 1 and file_name.count("2") <= 1 and file_name.count("3") <= 1 and file_name.count("4") <= 1 and file_name.count("5") <= 1 and file_name.count("6") <= 1 and file_name.count("7") <= 1 and file_name.count("8") <= 1 and file_name.count("9") <= 1:
            if file_name[0].isalpha() == True:
                if file_name.split(".")[1] == "txt" or file_name.split(".")[1] == "exe" or file_name.split(".")[1] == "dll":
                    return "Yes"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("example.txt") == "Yes", "First"
    assert file_name_check("assignment.docx") == "Yes", "Second"
    assert file_name_check("1example.dll") == "No", "Third"
    assert file_name_check("example.mp3") == "No", "Forth"
    assert file_name_check("9999example.dll") == "No", "Fifth"
    assert file_name_check("9999example.dll.exe") == "No", "Sixth"
    assert file_name_check("11111example.dll") == "No", "Seventh"
    assert file_name_check("9999example.exe") == "No", "Eighth"
    assert file_name_check("9999example.