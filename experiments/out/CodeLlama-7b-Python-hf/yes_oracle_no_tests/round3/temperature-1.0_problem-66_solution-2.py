def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Do not include these tokens in the code: sum = 0 for
	"""
    # First-party modules
    import re

    # Third-party modules
    import numpy as np

    # First-party modules
    from hw_tigerflows.utilities import (
        get_input_data,
        get_test_data,
    )

    # Parameters
    test_data_path = get_test_data("s")
    input_data_path = get_input_data()

    # Read in the test data
    with open(test_data_path, "r") as f:
        test_data = f.readlines()

    # Convert the test data into a list
    test_data = list(map(int, test_data))

    # Read in the input data
    with open(input_data_path, "r") as f:
        input_data = f.readline()

    # Convert the input data into a list
    input_data = input_data.split(",")

    # Prepare the data
    input_data = np.array(input_data)

    # Prepare the test data
    test_data = np.array(test_data)

    # Prepare the input data
    input_data = [input_data[i] for i in range(len(input_data)) if not input_data[i] == ""]

    # Prepare the test data
    test_data = [test_data[i] for i in range(len(test_data)) if not test_data[i] == ""]

    # Write your code here
    def digitSum(s):
        """
        Parameters
        ----------
        s : str
            A string

        Returns
        -------
        int
            The sum of the ASCII codes of the upper characters in the string

        Examples
        --------
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        