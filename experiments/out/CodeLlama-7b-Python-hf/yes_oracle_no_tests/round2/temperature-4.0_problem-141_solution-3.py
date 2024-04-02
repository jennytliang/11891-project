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

  # Please print out this 'pass' 
  # when you are ready to proceed
  # to the next session
  pass
  
  #==========================================
  # TODO: 2 - Create a variable called
  #        'number_of_digits' and assign it
  #        a value of 0
  #==========================================
  
  #==========================================
  # TODO: 3 - Write code that counts the
  #        number of digits in the file name
  #==========================================
  
  #==========================================
  # TODO: 4 - Write code that checks if the
  #        number of digits is greater than
  #        3. If it is, return 'No'.
  #==========================================
  
  #==========================================
  # TODO: 5 - Write code that checks if the
  #        file name has exactly one dot
  #        in it. If it doesn't, return 'No'.
  #==========================================
  
  #==========================================
  # TODO: 6 - Write code that checks if the
  #        substring before the dot is not
  #        empty. If it is, return 'No'.
  #==========================================
  
  #==========================================
  # TODO: 7 - Write code that checks if the
  #        character before the dot is a
  #        letter. If it isn't, return 'No'.
  #==========================================
  
  #==========================================
  # TODO: 8 - Write code that checks if the
  #        substring after the dot is one of
  #        the following: ['txt', 'exe', 'dll']
  #        If it isn't, return 'No'.
  #==========================================
  
  #==========================================
  # TODO: 9 - If the file name is valid,
  #        return 'Yes'. Otherwise, return
  #        'No'
  #==========================================



def main():
  """The main function is used to test your code.
  Do not change anything in this function!
  """
  print(file_