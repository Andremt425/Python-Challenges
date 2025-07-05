def CountVowels(s):
    """
    Get the total number of vowels in a string.
    
    Args:
    s (str): The string to check.
    
    Returns:
    int: Count of total vowels in a string.
    """

    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count