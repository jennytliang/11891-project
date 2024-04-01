def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    res = [ ]
    str = s.lower().replace(' ', ' ')
    
    for a in range( 0, len( str )):
      k = str[a]
      
      cnt = 0
      
      for vc in v:
        if str[a : a + 1].isalnum() is True and ( str[ a : a + 1 ] in v ) is False:
          cnt=cnt+1

      for i in v:  
        if i.lower() == str[ a ]:
          a+=1
          continue
                    
      if cnt == n:         
          temp = str[ : a ].strip()
          if temp is not "" and temp[ - 1 ] is not ' ':  
            res.append( temp.lower( ) )              
                    
        
    return( res )


