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
    # write your answer between #start and #end
    #start
    return 'Yes' if 0 < len(file_name) <= 3 and file_name.count('.') == 1 and file_name.endswith(('.txt', '.exe', '.dll')) and file_name[0].isalpha() else 'No'
    #end


if __name__ == '__main__':
    print('Example:')
    print(file_name_check('a.txt'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check('a.txt') == 'Yes'
    assert file_name_check('qweasdzxc.exe') == 'Yes'
    assert file_name_check('qweasdzxc.exe.txt') == 'No'
    assert file_name_check('3example.com') == 'No'
    assert file_name_check('.com') == 'No'
    assert file_name_check('') == 'No'
    assert file_name_check('a.b.c.d') == 'No'
    assert file_name_check('a') == 'No'
    assert file_name_check('999.exe') == 'No'
    print('You are awesome! All tests are done! Go Check it!')
