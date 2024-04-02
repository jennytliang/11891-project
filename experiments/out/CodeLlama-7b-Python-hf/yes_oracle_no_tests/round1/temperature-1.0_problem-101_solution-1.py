def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split()


def count_code_cells(ipynb = None):
    """
    You will be given a string of code that represents a Jupyter notebook in JSON format with the
    code cells that the Jupyter notebook contains. You need to count the number of code cells in 
    the dictionary (which represents the JSON notebook). Each code cell in
    the dictionary has the "cell_type" key and the corresponding value will either be 
    "code" or "markdown".

    Here is a sample code cell:
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {
            "collapsed": False
        },
        "outputs": [],
        "source": [
            "print(\"hello world\")"
        ]
    }
    
    Notes:
    If the cell type is "markdown", ignore it entirely.
    Each code cell will have a key "source" containing a list of strings with each string representing
    a single line of code.
    
    Parameters:
    ipynb (str): a JSON representation of a code cell 

    The return value should be an integer representing the number of code cells in a given
    notebook.
    
    Test case:
    count_code_cells(
    	'[{'
    	'    "cell_type": "code",'
    	'    "execution_count": 1,'
    	'    "metadata": {'
    	'        "collapsed": false'
    	'    },'
    	'    "outputs": [],'
    	'    "source":'
    	'        ["first line", "second line", "third line"]'
    	'}]'
    )
    return an integer of value 3.
    """
    # import json
    # # dict = json.loads(ipynb, fp)
    # dict = json.loads(ipynb)
    # count = 0
    # for i in list(dict):  # use dict to get a list
    #     a