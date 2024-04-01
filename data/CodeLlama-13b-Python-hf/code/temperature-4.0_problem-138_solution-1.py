def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # if len(list(divmod((n-20),20))) ==1:
        # return False  # return False if 

    if 2*(n//2) == n-8*(n//2):  # if the last digit is 0 then it is not True
      return True
      # else:  # if the last digit isn`t 0 then check whether the numbe is n-8*sum_of_all_even
      #   pass
    return False  # if it is smaller or bigger or both of the numbers n-8+n//4 are positive and have the rest of dividing 4 are equal  
  
  # def is_equal_to_sum_even(num=100):
  #     return 4*num % 16 == 0  # or 15 but 0 are not even numbers
