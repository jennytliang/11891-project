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
    # your code here
    import re
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif file_name.lower().startswith(r'[a-z]') is False:
        return 'No'
    elif file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("") == 'No', "Empty filename"
    assert file_name_check("myfile.txt") == 'Yes', "First"
    assert file_name_check("my.file.txt") == 'No', "Second"
    assert file_name_check("s.txt") == 'No', "Third"
    assert file_name_check("myfile.exe") == 'Yes', "Fourth"
    assert file_name_check("my.exe") == 'No', "Fifth"
    assert file_name_check("my.t") == 'No', "Sixth"
    assert file_name_check("my.dll") == 'Yes', "Seventh"
    assert file_name_check("myfile.dll.exe") == 'No', "Eighth"
    assert file_name_check("myfile.dll.exe.txt") == 'No', "Ninth"
    assert file_name_check(".myfile.txt") == 'No', "Tenth"
    assert file_name_check("txt.myfile") == 'No', "Eleventh"
    print('Done')
