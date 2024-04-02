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

  #YOUR CODE HERE
    import re
    
    a=file_name.split('.')
    if len(a)>3:
        return 'No'
    else:
        m=re.search("[a-zA-Z]",a[0])
        if '.' and '.txt' or '.dll' or '.exe' or '.' not in file_name:
            return 'No'
        if m is None:
            return 'No'
        else:
            return 'Yes'




print(file_name_check("example.dll")) # => 'No' (the name should start with a latin alphapet letter)"""

print(file_name_check("my.txt"))