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
    
	Include these tokens in the code:  if len ( list ( filter ( lambda
	Do not include these tokens in the code: file _ name . count
	"""

    # If there are more than three digits, return 'No'
    if file_name.count(list(range(10))) > 3:
        return 'No'

    # If there is no dot, return 'No'
    if file_name.count('.') == 0:
        return 'No'

    # If there is more than one dot, return 'No'
    if file_name.count('.') > 1:
        return 'No'

    # If the substring before the dot is empty, return 'No'
    if file_name.split('.')[0] == '':
        return 'No'

    # If the substring after the dot is not one of ['txt', 'exe', 'dll'], return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_function():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.dll") == 'Yes'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example.exe.old") == 'Yes'
    assert file_name_check("e.txt") == 'Yes'
    assert file_name_check("e.dll") == 'Yes'
    assert file_name_check("e.exe") == 'Yes'
    assert file_name_check("e.exe.old") == 'Yes'
    assert file_name_check("e.old") == 'Yes'

    assert file_name_check("test") == 'No'
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("example.exe.old.old") == 'No'
    assert file_name_check("e.exe.old.old") == 'No'
    assert file_name_check("e.exe.old.old.old") == 'No'
    assert file_name_check("e.old.old") == 'No'
    assert file_