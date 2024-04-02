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

 
    return 'Yes' if (file_name.count('.') == 1 and 
                     file_name.count('0') <= 3 and
                     file_name.count('1') <= 3 and
                     file_name.count('2') <= 3 and
                     file_name.count('3') <= 3 and
                     file_name.count('4') <= 3 and
                     file_name.count('5') <= 3 and
                     file_name.count('6') <= 3 and
                     file_name.count('7') <= 3 and
                     file_name.count('8') <= 3 and
                     file_name.count('9') <= 3 and
                     file_name.split('.')[0].strip() != '' and
                     file_name.split('.')[1].strip() in ['txt', 'exe', 'dll']) else 'No'


def file_size_check(file_size):
    """Create a function which takes a string representing the file's size, and returns
    'Yes' if the the file's size is valid, and returns 'No' otherwise.
    A file's size is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's size.
    - The file's size contains exactly one dot '.'
    - The substring before the dot should not be empty, and it should be a number.
    - The substring after the dot should be one of these: ['Kb', 'Mb', 'Gb']
    Examples:
    file_size_check("12.5Kb") # => 'Yes'
    file_size_check("12.5Gb") # => 'No' (the size should be in Kb, Mb or Gb)
    
	Include these tokens in the code: len ( list ( filter ( lambda ch : ch
	"""

    return 'Yes' if (file_size.count('.') == 1 and
                     file_size.count('0') <= 3 and