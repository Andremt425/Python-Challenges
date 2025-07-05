def CheckStringForPalindrome(string):
    """
    Check if a given string is a palindrome.
    
    Args:
    string (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: remove spaces and punctuation, convert to lowercase
    normalized_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_string == normalized_string[::-1]