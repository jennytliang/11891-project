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
    d ={}
    d['n'] =''
    i =0

    while i < len(message)  : 
       # print(i ," ", message[i] , "  ")
       if is_capital( message[i]  )  and  not(is_already_enc(message , d)) :
          new_key = swap_case(message[i])   
          add_key_new_val( dictionary , new_key , new_val_cap(new_key,i))



    return
       elif message[i] =="!" or message[i] =="@" :

   
   def encode (message):
    d = 
    
   d[0] = string.lower(message[:1])
  
