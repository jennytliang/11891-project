def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x>y:
        (x, y) = (y, x)
    flag = False
    number = x - 1
        
    while number != y:
          if (number<x):
              break
          else:    
              number = number-1
              if (number&1==True):
                  if (flag):
                      break
              else:
                  if number in range(x, y + 1):
                      flag = True
    
    if flag:
        return number
    else:
        return -1    