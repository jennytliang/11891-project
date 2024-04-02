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
    if file_name.count('.') > 1:
        return 'No'
    if file_name.count('.') < 1:
        return 'No'
    if file_name.count('.') == 1:
        if len(file_name.split('.')[1]) != 3:
            return 'No'
        if len(file_name.split('.')[0]) < 1:
            return 'No'
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        else:
            return 'Yes'


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))
    # => 'Yes'

    print(file_name_check("example.exe"))
    # => 'Yes'

    print(file_name_check("example.t"))
    # => 'No'

    print(file_name_check("example.e"))
    # => 'No'

    print(file_name_check("e.txt"))
    # => 'No'

    print(file_name_check("example.TXT"))
    # => 'Yes'

    print(file_name_check("example.txt.bak"))
    # => 'No'

    print(file_name_check("example.exe.bak"))
    # => 'No'

    print(file_name_check("example.dll.bak"))
    # => 'Yes'

    print(file_name_check("example.a.bak"))
    # => 'No'

    print(file_name_check("1example.txt"))
    # => 'No'

    print(file_name_check("example.txt1"))
    # => 'Yes'

    print(file_name_check(".txt"))
    # => 'No'

    print(file_name_check("txt."))
    # => 'No'

    print(file_name_check("1example1.txt"))
    #