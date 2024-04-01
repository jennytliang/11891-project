def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    pass


def g(t, n=None):
    '''
    Return the 2-dimensional list of size n with t numbers in it (or the default argument when not provided) and
    where the values in all rows are the same as the arguments of f function, in the order they returned them.
    The function takes three arguments, where the last one n defines the size of a matrix,
    if it not provided it is computed by using some other function h that returns a positive integer value
    :param t: values to be added to a matrix rows, t number of lists in a matrix to be filled with values
    :param n: values to fill into a matrix with rows equal to t, when provided, the size is n
    :return n x t matrix (a list of lists made of lists or lists of lists): a matrix of size t-rows x n-columns where
            all elements are f(i) if the element is of a list and the ith number if the number is a list.
    Example: 
        g(3) is a default call of a function which is computing n to call another function, but in this case n cannot
        be computed since f is not computed yet, but it should be the function call that will call the function when
        the function will get the correct arguments (1st function that calls the second and then it uses n as a
        parameter). Then a matrix of n*3 with its values filled like 3x3 matrix, 1 5, 2 6, 3 6,... in that order
        (values of lists from f can be used for 1st coordinate of a value of a matrix)
        '''
