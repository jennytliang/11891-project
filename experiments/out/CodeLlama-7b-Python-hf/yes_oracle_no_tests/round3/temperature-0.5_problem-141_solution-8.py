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
    
	Include these tokens in the code: if len ( list ( filter ( lambda ch
	Do not include these tokens in the code: def main (): print
	"""
    return 'Yes' if (file_name.count('.') == 1 and 
                      file_name.find('.') > 0 and
                      file_name.find('.') < len(file_name) - 4 and
                      file_name[0].isalpha() and
                      file_name[file_name.find('.') + 1:] in ['txt', 'exe', 'dll']) else 'No'
