def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    
    #vowels=("a" or "A" or
    message_list= [' ', 'a','e','i','o', 'u', 'b','c' , 'd',
                    'j', 'm' , 'n' ,  'q', 'r', 'x', 'v', 'w'
                  ,'y'+'z'+'1'+'2'+']3'+'{']
    vowel_swapper= ['0', 'A','E', 'H','I','D', 'Y', 'L', 'Z', '7', 'D', 'E','I','M','W']
    
    
    for x in xrange(len(message)):
        for y in xrange(len(message_list)):
            for vowels  in (message_list[y]+" "+message,message_list[y],
                                       "'"+message_list[vowel_swapper+y],"'"):
        print vowel_swap
            
'''
    if i=='a': 
        
    