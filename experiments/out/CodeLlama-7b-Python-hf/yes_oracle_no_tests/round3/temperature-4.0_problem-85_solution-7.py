def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: my _ list = lst
	"""
    # Add your code here
    return sum([lst[i] for i in range(len(lst)) if i % 2 != 0])


def main():
    print("Answer:", add([4, 2, 6, 7]))


if __name__ == "__main__":
    main()
