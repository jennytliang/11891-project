def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    number = str(num)
    n, o = len([d for d in number if d.isdigit and int(d) in range(2, 11)  % 2 == 0]), len (
        [d for d in number if d.isdigit and int(d) in range(1, 11) % 2 != 0])

    return (n, o), print('no of even and odd number digits', n, o, sep=', ')


def main():
    num = int(input("Enter a negative Integer: "))
    print (f"{even_odd_count(num)} {even_odd_count(num)[1]}")
    main()


if __name__ == '__main__':
    test = int(input("ENter the test integer number: "))   
    if test>=0:   # if the given test integer number is a positive number, or 0, ask the user to input negative number and run the main func again as asked by the question by the user
        num = int(input())
        main() 
               
