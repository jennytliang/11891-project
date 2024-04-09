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
    if file_name.count('.') > 1:
        return 'No'
    elif file_name.count('.') == 1 and file_name.count('0') > 3:
        return 'No'
    elif file_name.count('.') == 1 and file_name.count('0') <= 3:
        if file_name[0].isalpha() == True:
            if file_name.split('.')[-1] in ['txt', 'exe', 'dll']:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
    elif file_name.count('.') == 0 and file_name.count('0') <= 3:
        if file_name[0].isalpha() == True:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

if __name__ == '__main__':
    print('Example:')
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("web.folder.exe") == "No"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("web.folder.exe") == "No"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("web.folder.exe") == "No"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("web.folder.exe") == "No"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt") == "Yes"
   