def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple (' \ n \ r \ t
	'''
	# pass # Code goes here
    def find_spaces(txt):
      count = 0
      for i in txt:
        if i==" ":
          count = count + 1
      return count
    
    def find_commas():
      count = 0
      for i in txt:
        if i==",":
          count = count + 1
      return count
    
    
    def find_odd_order(letter):
      # print(ord(letter))
      return letter

    
    if find_spaces(txt) > 0:
      return txt.split(" ")
    elif find_commas(txt) > 0:
      return txt.split(",")
    else:
      
      n = 0
      for i in txt:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
          n = n + 1
      return n/2
    

  
    
  print(split_words("Hello World!"))
  # expected: ["Hello", "World!"]

  print(split_words("Hello,World!"))
  # expected: ["Hello", "World!"]
  
  print(split_words("abcdef"))
  # expected: 3
