def ReverseList(lst):
    """
    This function takes a list as input and returns a new list that is the reverse of the input list.
    
    :param lst: List to be reversed
    :return: New list that is the reverse of the input list
    """
    new_list = []
    for item in lst:
        new_list.insert(0, item)
    return new_list