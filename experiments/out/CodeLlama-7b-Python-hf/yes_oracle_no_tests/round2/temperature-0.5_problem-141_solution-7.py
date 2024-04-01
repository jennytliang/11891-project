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


    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the string method 'count'
    #    (https://docs.python.org/3/library/stdtypes.html#str.count)
    # -------------------------------------------------------------------------

    def file_name_check(file_name):
        if file_name.count('.') != 1:
            return 'No'
        elif file_name.count(' ') != 0:
            return 'No'
        elif file_name[0].isalnum() == False:
            return 'No'
        elif file_name[0].isalpha() == False:
            return 'No'
        elif len(file_name) > 3:
            return 'No'
        elif file_name.endswith('txt') or file_name.endswith('exe') or file_name.endswith('dll'):
            return 'Yes'
        else:
            return 'No'

    print(file_name_check('example.txt'))  # => 'Yes'
    print(file_name_check('1example.dll'))  # => 'No' (the name should start with a latin alphapet letter)





























































































































































































