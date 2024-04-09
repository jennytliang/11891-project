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
    
	Do not include these tokens in the code: # Please , insert your code
	"""
    # Code of the function
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return 'No'
    if file_name.count('A') > 3 or file_name.count('B') > 3 or file_name.count('C') > 3 or file_name.count('D') > 3 or file_name.count('E') > 3 or file_name.count('F') > 3 or file_name.count('G') > 3 or file_name.count('H') > 3 or file_name.count('I') > 3 or file_name.count('J') > 3 or file_name.count('K') > 3 or file_name.count('L') > 3 or file_name.count('M') > 3 or file_name.count('N') > 3 or file_name.count('O') > 3 or file_name.count('P') > 3 or file_name.count('Q') > 3 or file_name.count('R') > 3 or file_name.count('S') > 3 or file_name.count('T') > 3 or file_name.count('U') > 3 or file_name.count('V') > 3 or file_name.count('W') > 3 or file_name.count('X') > 3 or file_name.count('Y') > 3 or file_name.count('Z') > 3:
        return 'No'
    if file_name.count('a') > 3 or file_name.count('b') >