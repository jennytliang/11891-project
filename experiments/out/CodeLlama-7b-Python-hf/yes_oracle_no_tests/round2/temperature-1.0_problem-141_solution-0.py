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
    
    file_name = str(file_name)
    tokens = {'txt', 'exe', 'dll'}
    num_dict = {i: True for i in range(10, 40)}

    name, ext = (file_name.split(".")[:-1], file_name.split(".")[-1])

    return ("No " + chr(34) + "\'" + file_name + "\'" + chr(34) + " does not meet the rules.\n", None) if num_dict[
                                                                                                           name.count(
                                                                                                               "0")] or num_dict[
        name.count("1")] or num_dict[name.count("2")] or num_dict[name.count(
        "3")] or  name[0].isdigit() or ext not in tokens else ("Yes " + chr(
        34) + "\'" + file_name + "\'" + chr(34) + " is valid file name")


if __name__ == "__main__":
    print(file_name_check("1example.dll"))
    # expected result: "No '1example.dll' does not meet the rules."
    print()
    print(file_name_check("example.exe"))
    # expected reult: "Yes 'example.exe' is valid file name"
    print()
    print(file_name_check("MyProgram.txt"))
    # expected result: "Yes 'MyProgram.txt' is valid file name"