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

  count=0;
  count1=15;    
  for i in file_name:
  if (i.isalpha()):
   count=count+1;
  elif (i.isdigit() and count1>=10): 
   count1=count1-1;
  elif (i=='.'):
   if (count==0 or count>1 or count1>1 or  (i!= "exe"and not(i="txt")and not(i=='dll'))):
   
    if (count>1):
     return "No"      
   else:
    return "Yes"
  elif (i.isdigit() and count1<-15):
    return "No"
  elif (count==0):
  return "No"

file_name_check("example.py")
