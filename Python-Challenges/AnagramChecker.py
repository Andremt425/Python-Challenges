def AnagramChecker(word1, word2):
    """
    Check if two words are anagrams of each other.
    
    Args:
    word1 (str): The first word.
    word2 (str): The second word.
    
    Returns:
    bool: True if the words are anagrams, False otherwise.
    """
    return sorted(word1.lower()) == sorted(word2.lower())