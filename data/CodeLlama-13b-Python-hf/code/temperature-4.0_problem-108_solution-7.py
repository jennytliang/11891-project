def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    counter = 0

# loop through the array
# and if the current number > 0, we can use modulo operator, dividing that int by 2 until it has no remainder
# to check the digit 236 => 2%2===0; 117%2==1; 
# or you can try to cast it to binary using bin(). The first digit will represent the current signed digit of our number
# or you can convert a number into a signed representation using below formula (n+sign) where sign=-1 if first bit is 1; sign=0 else; 