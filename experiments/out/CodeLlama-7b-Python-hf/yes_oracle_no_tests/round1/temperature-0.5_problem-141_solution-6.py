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

    # Code here
    if file_name.count('.') == 1 and file_name.count('0') <= 3 and file_name.count('1') <= 3 and file_name.count('2') <= 3 and file_name.count('3') <= 3 and file_name.count('4') <= 3 and file_name.count('5') <= 3 and file_name.count('6') <= 3 and file_name.count('7') <= 3 and file_name.count('8') <= 3 and file_name.count('9') <= 3 and file_name.count('a') <= 3 and file_name.count('b') <= 3 and file_name.count('c') <= 3 and file_name.count('d') <= 3 and file_name.count('e') <= 3 and file_name.count('f') <= 3 and file_name.count('g') <= 3 and file_name.count('h') <= 3 and file_name.count('i') <= 3 and file_name.count('j') <= 3 and file_name.count('k') <= 3 and file_name.count('l') <= 3 and file_name.count('m') <= 3 and file_name.count('n') <= 3 and file_name.count('o') <= 3 and file_name.count('p') <= 3 and file_name.count('q') <= 3 and file_name.count('r') <= 3 and file_name.count('s') <= 3 and file_name.count('t') <= 3 and file_name.count('u') <= 3 and file_name.count('v') <= 3 and file_name.count('w') <= 3 and file_name.count('x') <= 3 and file_name.count('y') <= 3 and file_name.count('z') <= 3 and file_name.count('A') <= 3 and file_name.count('B') <= 3 and file_name.count('C') <= 3 and file_name.count('D') <= 3 and file_