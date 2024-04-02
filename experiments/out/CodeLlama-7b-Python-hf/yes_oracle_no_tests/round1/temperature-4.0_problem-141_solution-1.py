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
	"""
    result = "No"
    if file_name.count(".") == 1 and file_name.count("0") <= 3 and file_name.count("1") <= 3 and file_name.count("2") <= 3 and file_name.count("3") <= 3 and file_name.count("4") <= 3 and file_name.count("5") <= 3 and file_name.count("6") <= 3 and file_name.count("7") <= 3 and file_name.count("8") <= 3 and file_name.count("9") <= 3 and file_name.find(".") != 0 and file_name.find(".") != len(file_name) - 4 and file_name[-4:] in ["txt", "exe", "dll"]:
        result = "Yes"
    return result


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("web.html") == "Yes"
    assert file_name_check("web.htm") == "Yes"
    assert file_name_check("web.dmg") == "Yes"
    assert file_name_check("web.exe") == "Yes"
    assert file_name_check("web.TXT") == "Yes"
    assert file_name_check("web.bmp") == "No"
    assert file_name_check("web") == "No"
    assert file_name_check("1web.txt") == "No"
    assert file_name_check("web.1txt") == "No"
    assert file_name_check("web.1.txt") == "No"
    assert file_name_check("1web.1.txt") == "No"
    assert file_name_check("web.1.1.txt") == "No"
    assert file_name_check("1web.1